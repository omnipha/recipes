# AI Agent Host Recipe

Turns an Omnipha phone into an always-on headless host for autonomous AI coding and assistant agents.

## Stack

- **Node.js 22 & Python 3.12**: Runtime environments for agent toolchains.
- **Git & GitHub CLI**: Autonomous repository operations and pull requests.
- **tmux**: Persistent loopback sessions for worker monitoring and shift supervisor triggers.
- **ZRAM Swap**: Configured swap space to prevent OOM errors during compiler runs and agent reasoning passes.

## Configuration options (`omnipha.yaml`)

```yaml
recipes:
  - id: agent-host
    config:
      AGENT_FRAMEWORK: "openclaw"
      SWAP_SIZE_MB: 2048
```
