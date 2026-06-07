"""Microsoft Edge TTS plugin.

Wraps the free, high-quality neural TTS engine from Microsoft Edge as a
:class:`TTSProvider` implementation.

The heavy lifting — async ``edge_tts.Communicate`` invocation, voice/speed
resolution — lives in :mod:`tools.tts_tool`.  This plugin reaches into
that module via call-time indirection (``import tools.tts_tool as _tt``)
so:

* the existing test suite (``tests/tools/test_tts_tool.py``) keeps
  patching ``tools.tts_tool._generate_edge_tts`` /
  ``tools.tts_tool._import_edge_tts`` without modification, and
* there's exactly one canonical Edge TTS code path on disk — the plugin
  is a registration adapter, not a parallel implementation.

See the plugin-extraction-test-patch-compatibility rules this follows.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, List, Optional

from agent.tts_provider import TTSProvider

logger = logging.getLogger(__name__)


class EdgeTTSProvider(TTSProvider):
    """Microsoft Edge TTS backend.

    Delegates to ``tools.tts_tool._generate_edge_tts`` so the in-tree
    Edge TTS implementation (voice resolution, speed control, lazy
    ``edge_tts`` import) is the single source of truth.  Everything is
    resolved at call time via the ``_tt`` indirection so tests can
    monkey-patch the legacy module.
    """

    @property
    def name(self) -> str:
        return "edge"

    @property
    def display_name(self) -> str:
        return "Microsoft Edge TTS"

    def is_available(self) -> bool:
        # Edge TTS is always available — no API key required.
        # Only check that the edge_tts package is importable.
        try:
            import tools.tts_tool as _tt
            _tt._import_edge_tts()
            return True
        except Exception:  # noqa: BLE001 — defensive; never break the picker
            return False

    def get_setup_schema(self) -> Dict[str, Any]:
        return {
            "name": "Microsoft Edge TTS",
            "badge": "★ recommended · free",
            "tag": "Free, high-quality neural TTS via Microsoft Edge",
            "env_vars": [],
        }

    def list_voices(self) -> List[Dict[str, Any]]:
        """Return the Edge TTS voice catalog.

        ``edge_tts.list_voices()`` is an async coroutine that fetches
        the full catalog from Microsoft's endpoint.  We run it
        synchronously here — the caller (``hermes tools``, voice
        picker) is not in an async context.
        """
        try:
            import tools.tts_tool as _tt
            _edge_tts = _tt._import_edge_tts()
            voices = asyncio.run(_edge_tts.list_voices())
            return [
                {
                    "id": v.get("ShortName", v.get("Name", "")),
                    "display": v.get("FriendlyName", v.get("ShortName", "")),
                    "language": v.get("Locale", ""),
                    "gender": v.get("Gender", "").lower(),
                }
                for v in voices
            ]
        except Exception:  # noqa: BLE001
            logger.debug("Edge TTS list_voices failed", exc_info=True)
            return []

    def synthesize(
        self,
        text: str,
        output_path: str,
        *,
        voice: Optional[str] = None,
        model: Optional[str] = None,
        speed: Optional[float] = None,
        format: str = "mp3",
        **extra: Any,
    ) -> str:
        """Synthesize ``text`` via the legacy Edge TTS pipeline.

        Forwards to :func:`tools.tts_tool._generate_edge_tts`, which
        handles voice selection, speed adjustment, and the async
        ``edge_tts.Communicate.save()`` call.
        """
        import tools.tts_tool as _tt

        # Build a tts_config dict that _generate_edge_tts expects.
        tts_config: Dict[str, Any] = {}
        edge_config: Dict[str, Any] = {}
        if voice is not None:
            edge_config["voice"] = voice
        if speed is not None:
            edge_config["speed"] = speed
            tts_config["speed"] = speed
        if edge_config:
            tts_config["edge"] = edge_config

        return asyncio.run(_tt._generate_edge_tts(text, output_path, tts_config))


# ---------------------------------------------------------------------------
# Plugin entry point
# ---------------------------------------------------------------------------


def register(ctx) -> None:
    """Plugin entry point — wire ``EdgeTTSProvider`` into the registry."""
    ctx.register_tts_provider(EdgeTTSProvider())
