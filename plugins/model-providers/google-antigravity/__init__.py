"""Google Antigravity OAuth provider profile for Hermes Agent.

This plugin registers the `google-antigravity` model provider profile. Runtime
OAuth and transport support is supplied by the companion Hermes core patch in
this repository until Hermes exposes plugin hooks for custom OAuth resolvers and
model clients.
"""

from __future__ import annotations

from typing import Any

from providers import register_provider
from providers.base import ProviderProfile


class GoogleAntigravityProfile(ProviderProfile):
    """Google Antigravity OAuth profile.

    Antigravity uses the Cloud Code PA transport shape, but with Antigravity
    OAuth credentials, headers, model IDs, and UI thinking tier semantics.
    """

    def build_extra_body(
        self, *, session_id: str | None = None, **context: Any
    ) -> dict[str, Any]:
        extra: dict[str, Any] = {}
        if session_id:
            extra["session_id"] = session_id

        # Antigravity's runtime client consumes the same top-level
        # ``thinking_config`` shape as Cloud Code Assist.  Keep this logic in
        # the provider profile path because registered providers bypass the
        # legacy ``provider_name == \"google-antigravity\"`` branch in the
        # chat-completions transport.
        from agent.transports.chat_completions import _build_antigravity_thinking_config

        model = str(context.get("model") or "")
        reasoning_config = context.get("reasoning_config")
        thinking_config = _build_antigravity_thinking_config(model, reasoning_config)
        if thinking_config:
            extra["thinking_config"] = thinking_config
        return extra


google_antigravity = GoogleAntigravityProfile(
    name="google-antigravity",
    aliases=("antigravity", "antigravity-oauth"),
    display_name="Google Antigravity (OAuth)",
    description="Google Antigravity via OAuth + Code Assist; no Gemini CLI dependency.",
    api_mode="chat_completions",
    env_vars=(),
    base_url="cloudcode-pa://antigravity",
    auth_type="oauth_external",
    supports_health_check=False,
    fallback_models=(
        "gemini-3.5-flash",
        "gemini-3.1-pro",
        "claude-sonnet-4-6",
        "claude-opus-4-6",
        "gpt-oss-120b",
    ),
)

register_provider(google_antigravity)
