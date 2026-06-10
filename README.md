<p align="center">
  <img src="assets/banner.png" alt="Hermes Agent" width="100%">
</p>

# Hermes Agent ☤
<p align="center">
  <a href="https://hermes-agent.nousresearch.com/">Hermes Agent</a> | <a href="https://hermes-agent.nousresearch.com/">Hermes Desktop</a>
</p>
<p align="center">
  <a href="https://Meapri.github.io/hermes-agent-plus/docs/"><img src="https://img.shields.io/badge/Docs-hermes--agent--plus-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://discord.gg/NousResearch"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/Meapri/hermes-agent-plus/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://nousresearch.com"><img src="https://img.shields.io/badge/Built%20by-Nous%20Research-blueviolet?style=for-the-badge" alt="Built by Nous Research"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/Lang-中文-red?style=for-the-badge" alt="中文"></a>
  <a href="README.ur-pk.md"><img src="https://img.shields.io/badge/Lang-اردو-green?style=for-the-badge" alt="اردو"></a>
</p>

## ✨ Hermes Agent Plus (Meapri 포크) 주요 특징

본 저장소(`Meapri/hermes-agent-plus`)는 공식 저장소를 기반으로 한국인 사용자 편의성을 극대화하기 위해 다음과 같은 고유 기능이 추가된 포크 버전입니다:

1. **완벽한 한글화 (Full Korean Localization):**
   - **문서 및 가이드:** 모든 공식 문서와 README가 한글화되어 있으며, [전용 GitHub Pages](https://Meapri.github.io/hermes-agent-plus/docs/)를 통해 호스팅됩니다.
   - **데스크톱 및 CLI 앱:** 기본 언어가 한국어(`ko`)로 설정되어 있어 복잡한 설정 없이 바로 한국어 UI와 안내 메시지를 사용할 수 있습니다.
2. **Claude 인증 및 결제 우회 (Claude Auth & Billing Bypass):**
   - 코드 레벨(`anthropic_adapter.py`, `anthropic_billing_bypass.py`)에서 Anthropic API의 결제 및 권한 확인 루틴을 자체적으로 우회 및 호환하도록 완전 통합(Native Integration)되어 있습니다.
3. **독자적인 원클릭 설치 환경:**
   - 공식 저장소가 아닌 본 포크 저장소의 수정된 코드베이스를 즉시 다운로드하고 세팅하도록 커스텀된 `install.sh` 및 `install.ps1` 스크립트를 제공합니다.
4. **Google Antigravity 기본 통합 (Antigravity Provider Integration):**
   - 구글 내부망 기반의 Antigravity 제공자를 공식 지원하도록 어댑터 및 인증 로직이 내장되어 있습니다. `hermes model` 명령어를 통해 언제든지 전환하여 활용할 수 있습니다.
5. **Antigravity 비동기 자율 팀 (Antigravity Async Team Orchestration):**
   - 레거시 동기식 `delegate_task`를 걷어내고, 메인 에이전트의 작업을 막지 않고 독립적으로 동작하는 `spawn_subagent`, `manage_subagents`, `send_message` 도구로 전면 개편되었습니다.
6. **데스크톱 UI 마크다운 확장 렌더링:**
   - 데스크톱 UI에서 Mermaid 다이어그램, 정보 슬라이드(Carousel) 및 GitHub 스타일 Alert 요소를 예쁘게 보여주는 커스텀 렌더러가 내장되어 있습니다.

---

**[Nous Research](https://nousresearch.com)가 만든 스스로 발전하는 AI 에이전트입니다.** 경험을 통해 스킬을 만들고, 사용하는 동안 이를 개선하며, 지식을 지속적으로 기억하도록 유도하고, 이전 대화를 검색하여 여러 세션에 걸쳐 당신이 누구인지 모델링하는 내장형 학습 루프를 갖춘 유일한 에이전트입니다. 5달러짜리 VPS, GPU 클러스터, 또는 유휴 상태일 때 거의 비용이 들지 않는 서버리스 인프라에서 실행해 보세요. 노트북에 얽매이지 않고, 클라우드 VM에서 작업하는 동안 텔레그램을 통해 에이전트와 대화할 수 있습니다.

[Nous Portal](https://portal.nousresearch.com), [OpenRouter](https://openrouter.ai) (200개 이상 모델), [NovitaAI](https://novita.ai) (모델 API, 에이전트 샌드박스, GPU 클라우드를 위한 AI 네이티브 클라우드), [NVIDIA NIM](https://build.nvidia.com) (Nemotron), [Xiaomi MiMo](https://platform.xiaomimimo.com), [z.ai/GLM](https://z.ai), [Kimi/Moonshot](https://platform.moonshot.ai), [MiniMax](https://www.minimax.io), [Hugging Face](https://huggingface.co), OpenAI 등 원하는 모델 또는 자체 엔드포인트를 사용하세요. 코드 변경이나 락인(lock-in) 없이 `hermes model` 명령어로 쉽게 전환할 수 있습니다.

<table>
<tr><td><b>완벽한 터미널 인터페이스</b></td><td>멀티라인 편집, 슬래시 명령어 자동완성, 대화 기록, 중단 및 리디렉션, 실시간 도구 출력 스트리밍을 지원하는 완전한 TUI를 제공합니다.</td></tr>
<tr><td><b>당신이 있는 곳 어디서나</b></td><td>단일 게이트웨이 프로세스에서 텔레그램, 디스코드, 슬랙, WhatsApp, 시그널, CLI 등 모든 플랫폼을 지원합니다. 음성 메모 텍스트 변환 및 크로스 플랫폼 대화 지속성을 지원합니다.</td></tr>
<tr><td><b>닫힌 학습 루프</b></td><td>주기적인 프롬프트를 통해 에이전트가 관리하는 메모리. 복잡한 작업 후 스스로 스킬을 생성합니다. 스킬은 사용하는 동안 발전합니다. 크로스 세션 리콜을 위해 LLM 요약과 함께 FTS5 세션 검색을 지원합니다. <a href="https://github.com/plastic-labs/honcho">Honcho</a> 기반 다이얼로그 사용자 모델링 기능. <a href="https://agentskills.io">agentskills.io</a> 개방형 표준과 호환됩니다.</td></tr>
<tr><td><b>예약 자동화</b></td><td>내장 크론(cron) 스케줄러를 통해 원하는 플랫폼으로 결과를 전달합니다. 자연어를 사용해 무인으로 실행되는 일일 보고서, 야간 백업, 주간 감사를 설정하세요.</td></tr>
<tr><td><b>위임 및 병렬 처리</b></td><td>격리된 하위 에이전트를 생성해 작업을 병렬로 처리합니다. RPC를 통해 도구를 호출하는 파이썬 스크립트를 작성하여 여러 단계의 파이프라인을 컨텍스트 비용 없는 턴으로 압축할 수 있습니다.</td></tr>
<tr><td><b>어디서든 실행 (노트북뿐만 아니라)</b></td><td>로컬, Docker, SSH, Singularity, Modal, Daytona 등 6가지 터미널 백엔드를 지원합니다. Daytona와 Modal은 서버리스 지속성을 제공하여, 에이전트의 환경이 유휴 상태일 때 최대 절전 모드로 전환되고 요청 시에만 활성화되어 세션 사이에 비용이 거의 발생하지 않습니다. 5달러짜리 VPS나 GPU 클러스터에서 실행하세요.</td></tr>
<tr><td><b>연구 준비 완료</b></td><td>차세대 툴 호출 모델 학습을 위한 배치 궤적(trajectory) 생성 및 궤적 압축 기능.</td></tr>
</table>

---

## 빠른 설치 (Quick Install)

### Linux, macOS, WSL2, Termux

```bash
curl -fsSL https://raw.githubusercontent.com/Meapri/hermes-agent-plus/main/scripts/install.sh | bash
```

### Windows (네이티브, PowerShell)

> **참고:** 네이티브 Windows는 WSL 없이 Hermes를 실행합니다. CLI, 게이트웨이, TUI 및 도구 모두 네이티브로 작동합니다. 만약 WSL2를 선호한다면, 위의 Linux/macOS 명령어 한 줄로 설치할 수도 있습니다. 버그를 발견하셨나요? [이슈를 등록](https://github.com/Meapri/hermes-agent-plus/issues)해 주세요.

PowerShell에서 아래 명령어를 실행하세요:

```powershell
iex (irm https://raw.githubusercontent.com/Meapri/hermes-agent-plus/main/scripts/install.ps1)
```

이 설치 프로그램은 uv, Python 3.11, Node.js, ripgrep, ffmpeg, **그리고 포터블 Git Bash** (MinGit을 `%LOCALAPPDATA%\hermes\git`에 압축 해제하며 관리자 권한이 필요 없고 기존 시스템 Git 설치와 완전히 격리됨) 등 모든 것을 자동으로 처리합니다. Hermes는 쉘 명령을 실행하기 위해 내장된 Git Bash를 사용합니다.

시스템에 Git이 이미 설치되어 있다면, 설치 프로그램이 이를 감지하여 대신 사용합니다. 그렇지 않다면 ~45MB의 MinGit 다운로드만으로 충분하며, 시스템의 기존 Git에는 영향을 주지 않습니다.

> **Android / Termux:** 검증된 수동 설치 과정은 [Termux 가이드](https://Meapri.github.io/hermes-agent-plus/docs/getting-started/termux)에 문서화되어 있습니다. Termux에서는 전체 `.[all]` 패키지가 현재 Android와 호환되지 않는 음성 의존성을 포함하므로, 최적화된 `.[termux]` 패키지를 설치합니다.
>
> **Windows:** 네이티브 Windows가 완벽하게 지원됩니다 — 위의 PowerShell 명령어 한 줄로 모두 설치됩니다. WSL2를 선호한다면 Linux 명령어를 사용할 수도 있습니다. 네이티브 Windows 설치 경로는 `%LOCALAPPDATA%\hermes`에 있으며, WSL2는 Linux와 같이 `~/.hermes`에 설치됩니다. 현재 브라우저 기반 대시보드 채팅창 기능만 POSIX PTY를 사용하기 위해 특별히 WSL2가 필요합니다(기본 CLI 및 게이트웨이는 네이티브로 실행됩니다).

설치 후:

```bash
source ~/.bashrc    # 쉘 설정 다시 불러오기 (또는: source ~/.zshrc)
hermes              # 대화 시작!
```

---

## 시작하기 (Getting Started)

```bash
hermes              # 대화형 CLI — 대화 시작
hermes model        # LLM 제공자 및 모델 선택
hermes tools        # 활성화할 도구 설정
hermes config set   # 개별 설정 값 세팅
hermes gateway      # 메시징 게이트웨이 시작 (Telegram, Discord 등)
hermes setup        # 전체 설정 마법사 실행 (모든 구성을 한 번에 설정)
hermes claw migrate # OpenClaw에서 마이그레이션 (OpenClaw 사용자용)
hermes update       # 최신 버전으로 업데이트
hermes doctor       # 문제 진단
```

📖 **[전체 문서 보기 →](https://Meapri.github.io/hermes-agent-plus/docs/)**

---

## API 키 수집 생략 — Nous Portal

Hermes는 여러분이 원하는 어떠한 제공자와도 함께 동작합니다 — 이 사실은 변함이 없습니다. 하지만 모델, 웹 검색, 이미지 생성, 텍스트 음성 변환(TTS), 클라우드 브라우저를 위해 다섯 개의 각기 다른 API 키를 모으기 귀찮다면, **[Nous Portal](https://portal.nousresearch.com)** 구독 하나로 모든 것을 처리할 수 있습니다:

- **300개 이상의 모델** — `/model <이름>` 명령어로 선택 가능
- **Tool Gateway (도구 게이트웨이)** — 웹 검색 (Firecrawl), 이미지 생성 (FAL), 텍스트 음성 변환 (OpenAI), 클라우드 브라우저 (Browser Use) 기능이 모두 구독 하나로 라우팅됩니다. 추가 계정이 필요 없습니다.

새로 설치한 후 단 한 번의 명령어로 가능합니다:

```bash
hermes setup --portal
```

위 명령어는 OAuth를 통해 로그인하고, Nous를 제공자로 설정하며, Tool Gateway를 활성화합니다. 연결된 서비스 상태는 언제든지 `hermes portal info` 명령어로 확인할 수 있습니다. 자세한 내용은 [Tool Gateway 문서 페이지](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/features/tool-gateway)에서 확인할 수 있습니다.

물론 원한다면 언제든지 개별 도구마다 기존의 API 키를 가져와 사용할 수 있습니다 — 게이트웨이는 백엔드별로 설정되므로 꼭 전부를 사용할 필요는 없습니다.

---

## CLI vs 메시징 빠른 참고

Hermes에는 두 가지 진입점이 있습니다: `hermes` 명령어로 터미널 UI를 시작하거나, 게이트웨이를 실행하여 Telegram, Discord, Slack, WhatsApp, Signal 또는 이메일에서 대화할 수 있습니다. 대화가 시작되면 대부분의 슬래시 명령어는 양쪽 인터페이스에서 동일하게 공유됩니다.

| 액션 (Action)                         | CLI                                           | 메시징 플랫폼 (Messaging platforms)                                                              |
| ------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 대화 시작                             | `hermes`                                      | `hermes gateway setup` + `hermes gateway start` 실행 후 봇에게 메시지 전송                       |
| 새로운 대화 시작                      | `/new` 또는 `/reset`                          | `/new` 또는 `/reset`                                                                             |
| 모델 변경                             | `/model [제공자:모델]`                        | `/model [제공자:모델]`                                                                           |
| 페르소나 설정                         | `/personality [이름]`                         | `/personality [이름]`                                                                            |
| 마지막 턴 재시도 또는 취소            | `/retry`, `/undo`                             | `/retry`, `/undo`                                                                                |
| 컨텍스트 압축 / 사용량 확인           | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]`                                                        |
| 스킬 찾아보기                         | `/skills` 또는 `/<스킬-이름>`                 | `/<스킬-이름>`                                                                                   |
| 현재 작업 중단                        | `Ctrl+C` 또는 새 메시지 전송                  | `/stop` 또는 새 메시지 전송                                                                      |
| 플랫폼별 상태 확인                    | `/platforms`                                  | `/status`, `/sethome`                                                                            |

전체 명령어 목록은 [CLI 가이드](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/cli)와 [메시징 게이트웨이 가이드](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/messaging)에서 확인하세요.

---

## 문서 (Documentation)

모든 문서는 **[Meapri.github.io/hermes-agent-plus/docs](https://Meapri.github.io/hermes-agent-plus/docs/)** 에서 확인할 수 있습니다:

| 섹션                                                                                             | 다루는 내용                                             |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [Quickstart (빠른 시작)](https://Meapri.github.io/hermes-agent-plus/docs/getting-started/quickstart)                 | 2분 안에 설치 → 설정 → 첫 대화 시작하기          |
| [CLI Usage (CLI 사용법)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/cli)                              | 명령어, 단축키, 페르소나, 세션             |
| [Configuration (환경 설정)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/configuration)                | 설정 파일, 제공자, 모델 등 모든 옵션                |
| [Messaging Gateway (메시징 게이트웨이)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/messaging)                | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| [Security (보안)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/security)                          | 명령어 승인, DM 페어링, 컨테이너 격리          |
| [Tools & Toolsets (도구 및 도구 세트)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/features/tools)            | 40개 이상의 도구, 도구 세트 시스템, 터미널 백엔드               |
| [Skills System (스킬 시스템)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/features/skills)              | 절차적 기억, 스킬 허브, 스킬 만들기             |
| [Memory (메모리)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/features/memory)                     | 영구 메모리, 사용자 프로필, 모범 사례           |
| [MCP Integration (MCP 통합)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/features/mcp)               | 모든 MCP 서버를 연결하여 확장된 기능 제공           |
| [Cron Scheduling (크론 예약 자동화)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/features/cron)              | 플랫폼 전달이 포함된 예약된 작업                     |
| [Context Files (컨텍스트 파일)](https://Meapri.github.io/hermes-agent-plus/docs/user-guide/features/context-files)       | 모든 대화의 형태를 잡아주는 프로젝트 컨텍스트             |
| [Architecture (아키텍처)](https://Meapri.github.io/hermes-agent-plus/docs/developer-guide/architecture)             | 프로젝트 구조, 에이전트 루프, 주요 클래스                 |
| [Contributing (기여하기)](https://Meapri.github.io/hermes-agent-plus/docs/developer-guide/contributing)             | 개발 설정, PR 프로세스, 코드 스타일                  |
| [CLI Reference (CLI 명령어 참조)](https://Meapri.github.io/hermes-agent-plus/docs/reference/cli-commands)                  | 모든 명령어 및 플래그                                     |
| [Environment Variables (환경 변수)](https://Meapri.github.io/hermes-agent-plus/docs/reference/environment-variables) | 전체 환경 변수 참조                                 |

---

## OpenClaw에서 마이그레이션

OpenClaw를 사용 중이라면, Hermes가 여러분의 설정, 메모리, 스킬 및 API 키를 자동으로 가져올 수 있습니다.

**최초 설정 중:** 설정 마법사(`hermes setup`)가 `~/.openclaw` 폴더를 자동으로 감지하고 본격적인 구성 전에 마이그레이션을 제안합니다.

**설치 후 언제든지:**

```bash
hermes claw migrate              # 대화형 마이그레이션 (전체 프리셋)
hermes claw migrate --dry-run    # 어떤 내용이 마이그레이션 될지 미리보기
hermes claw migrate --preset user-data   # 시크릿(비밀번호/키) 제외하고 마이그레이션
hermes claw migrate --overwrite  # 기존 충돌 내용 덮어쓰기
```

가져오는 항목들:

- **SOUL.md** — 페르소나 파일
- **Memories** — MEMORY.md 및 USER.md 항목
- **Skills** — 사용자가 만든 스킬 → `~/.hermes/skills/openclaw-imports/`
- **Command allowlist** — 명령어 허용 승인 패턴
- **Messaging settings** — 플랫폼 구성, 허용된 사용자, 작업 디렉토리
- **API keys** — 허용 목록에 있는 시크릿 키 (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)
- **TTS assets** — 작업 공간 오디오 파일
- **Workspace instructions** — AGENTS.md (`--workspace-target` 사용 시)

전체 옵션을 보려면 `hermes claw migrate --help`를 참조하거나, `openclaw-migration` 스킬을 사용하여 드라이 런 미리보기 기능이 포함된 대화형 에이전트 기반 마이그레이션을 진행해 보세요.

---

## 기여하기 (Contributing)

여러분의 기여를 환영합니다! 개발 환경 설정, 코드 스타일, PR 진행 과정은 [기여 가이드(Contributing Guide)](https://Meapri.github.io/hermes-agent-plus/docs/developer-guide/contributing)에서 확인하세요.

기여자들을 위한 빠른 시작 — `setup-hermes.sh`로 클론하고 바로 시작하세요:

```bash
git clone https://github.com/Meapri/hermes-agent-plus.git
cd hermes-agent
./setup-hermes.sh     # uv 설치, 가상환경(venv) 생성, .[all] 설치, ~/.local/bin/hermes 심볼릭 링크 생성
./hermes              # 가상환경을 자동 감지하므로 'source' 명령어를 먼저 실행할 필요 없음
```

수동 설정 방법 (위 명령어와 동일):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

---

## 커뮤니티 (Community)

- 💬 [Discord](https://discord.gg/NousResearch)
- 📚 [Skills Hub](https://agentskills.io)
- 🐛 [Issues](https://github.com/Meapri/hermes-agent-plus/issues)
- 🔌 [computer-use-linux](https://github.com/avifenesh/computer-use-linux) — Hermes 및 다른 MCP 호스트를 위한 리눅스 데스크톱 제어 MCP 서버. AT-SPI 접근성 트리, Wayland/X11 입력, 스크린샷 캡처 및 컴포지터 창 지정 기능 지원.
- 🔌 [HermesClaw](https://github.com/AaronWong1999/hermesclaw) — 커뮤니티 개발 WeChat 브릿지: 동일한 WeChat 계정에서 Hermes Agent와 OpenClaw를 동시에 실행하세요.

---

## 라이선스 (License)

MIT — [LICENSE](LICENSE)를 참조하세요.

Built by [Nous Research](https://nousresearch.com).
