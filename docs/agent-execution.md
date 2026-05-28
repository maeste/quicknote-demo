# Agent Execution & Sandbox Policy

> How AI coding agents should run commands against this repo safely.
> Vendor-neutral: pick whichever sandbox fits your setup.

## Recommended isolation (choose one)

- **devcontainer** — `.devcontainer/` in this repo gives a reproducible,
  network-restricted container. Open in VS Code / Codespaces.
- **OS sandbox** — macOS `sandbox-exec`, Linux `bubblewrap`/`firejail`, or your
  agent's built-in sandbox mode (e.g. Codex `sandbox_mode`).
- **Hosted sandbox** — run the agent in an ephemeral cloud VM.
- **[LINCE](https://lince.sh)** — host-level sandbox that wraps the agent process
  with a default-deny policy. One good option among the above.

Runtime sandbox usage can't be detected by a repo scan — documenting the policy
here is how this project earns credit for it.

## Safe-to-run commands

These are read-only or test-scoped and safe for an agent to run unattended:

```bash
pytest
ruff check .
ruff format --check .
mypy
git status
git diff
```

## Requires human approval

- Anything that writes outside the working tree
- Network calls beyond package installs
- `git push`, releases, or changing CI/secrets

## Secrets

Never read or print real secrets. Copy `.env.example` → `.env` (gitignored) for
local values. Secret patterns are covered in `.gitignore`; gitleaks runs in
pre-commit.
