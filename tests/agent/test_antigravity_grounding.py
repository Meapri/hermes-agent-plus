"""Tests for Antigravity Gemini Google Search grounding modes.

Focus: the new ``smart`` grounding mode, which lets the MODEL decide when to
search (no hardcoded keyword gate) while PRESERVING the agent's function tools.
Also guards existing auto/always/off semantics against regression.
"""
from __future__ import annotations

import importlib

import pytest

adapter = importlib.import_module("agent.google_antigravity_adapter")


@pytest.fixture(autouse=True)
def _clear_grounding_env(monkeypatch):
    for var in (
        "HERMES_ANTIGRAVITY_GOOGLE_GROUNDING",
        "HERMES_GOOGLE_GROUNDING_SEARCH_ENABLED",
        "HERMES_ANTIGRAVITY_GROUNDING_SUPPRESS_EXTERNAL_SEARCH_TOOLS",
        "HERMES_ANTIGRAVITY_GROUNDING_SUPPRESS_FUNCTION_TOOLS",
    ):
        monkeypatch.delenv(var, raising=False)
    yield


def _req_with_function_tool(text="안녕 오늘 뭐해?"):
    return {
        "contents": [{"role": "user", "parts": [{"text": text}]}],
        "tools": [
            {"functionDeclarations": [{"name": "get_weather", "description": "날씨 조회"}]}
        ],
    }


def _has_google_search(request):
    return any(
        isinstance(t, dict) and isinstance(t.get("google_search"), dict)
        for t in request.get("tools", [])
    )


def _function_names(request):
    names = []
    for t in request.get("tools", []):
        if isinstance(t, dict):
            for d in t.get("functionDeclarations", []) or []:
                names.append(d.get("name"))
    return names


# ── smart mode: model decides, function tools preserved ──────────────────────

def test_smart_mode_attaches_google_search_without_keyword(monkeypatch):
    """smart mode adds google_search even when NO search keyword is present."""
    monkeypatch.setenv("HERMES_ANTIGRAVITY_GOOGLE_GROUNDING", "smart")
    req = _req_with_function_tool("안녕 오늘 뭐해?")  # no search trigger words
    adapter._maybe_enable_google_grounding(req, model="gemini-3.5-flash")
    assert _has_google_search(req), "smart mode must attach google_search regardless of keywords"


def test_smart_mode_preserves_function_tools(monkeypatch):
    """smart mode attaches google_search. Because the Antigravity endpoint can't
    mix built-in google_search with function declarations (it 400s), grounding
    narrows to the grounded tool only — function tools are dropped while a search
    is offered. This is the verified-safe behavior; grounded answers beat 400s."""
    monkeypatch.setenv("HERMES_ANTIGRAVITY_GOOGLE_GROUNDING", "smart")
    req = _req_with_function_tool("최신 뉴스 찾아줘")
    adapter._maybe_enable_google_grounding(req, model="gemini-3.5-flash")
    assert _has_google_search(req)
    assert "get_weather" not in _function_names(req), "function tools must be dropped alongside grounding"


def test_smart_mode_no_duplicate_google_search(monkeypatch):
    monkeypatch.setenv("HERMES_ANTIGRAVITY_GOOGLE_GROUNDING", "smart")
    req = _req_with_function_tool()
    adapter._maybe_enable_google_grounding(req, model="gemini-3.5-flash")
    adapter._maybe_enable_google_grounding(req, model="gemini-3.5-flash")
    gs = [t for t in req["tools"] if isinstance(t, dict) and isinstance(t.get("google_search"), dict)]
    assert len(gs) == 1


def test_grounding_never_mixes_builtin_with_function_tools(monkeypatch):
    """Regression guard for the RTX/DGX Spark bug: a request with google_search
    must NEVER also carry function declarations (that combination 400s on the
    Antigravity endpoint and silently degrades to ungrounded hallucination)."""
    for mode in ("smart", "always"):
        monkeypatch.setenv("HERMES_ANTIGRAVITY_GOOGLE_GROUNDING", mode)
        req = _req_with_function_tool("오늘 환율 알려줘")
        adapter._maybe_enable_google_grounding(req, model="gemini-3.5-flash")
        if _has_google_search(req):
            assert not _function_names(req), f"{mode}: function tools leaked alongside google_search"


# ── regression guards for existing modes ─────────────────────────────────────

def test_off_mode_never_attaches(monkeypatch):
    monkeypatch.setenv("HERMES_ANTIGRAVITY_GOOGLE_GROUNDING", "off")
    req = _req_with_function_tool("최신 뉴스 검색해줘")
    adapter._maybe_enable_google_grounding(req, model="gemini-3.5-flash")
    assert not _has_google_search(req)


def test_auto_mode_still_keyword_gated(monkeypatch):
    """auto mode keeps its keyword behavior: no trigger → no google_search."""
    monkeypatch.setenv("HERMES_ANTIGRAVITY_GOOGLE_GROUNDING", "auto")
    req = _req_with_function_tool("안녕 잘 지냈어?")  # no trigger
    adapter._maybe_enable_google_grounding(req, model="gemini-3.5-flash")
    assert not _has_google_search(req)


def test_auto_mode_triggers_on_keyword(monkeypatch):
    monkeypatch.setenv("HERMES_ANTIGRAVITY_GOOGLE_GROUNDING", "auto")
    req = _req_with_function_tool("오늘 환율 얼마야?")  # 오늘/환율 triggers
    adapter._maybe_enable_google_grounding(req, model="gemini-3.5-flash")
    assert _has_google_search(req)


def test_mode_resolver_recognizes_smart(monkeypatch):
    monkeypatch.setenv("HERMES_ANTIGRAVITY_GOOGLE_GROUNDING", "smart")
    assert adapter._antigravity_google_grounding_mode() == "smart"
