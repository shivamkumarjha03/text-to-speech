## Quick context for AI coding agents

Repository state: no source files detected at time of writing. These instructions prioritize fast discovery steps and pragmatic rules for contributing when the codebase is empty or partially scaffolded.

1) First-actions (do these immediately)
- Run a recursive file manifest to discover top-level manifests, build files, and CI. Example (PowerShell):

```powershell
Get-ChildItem -Recurse -Force -File | Select-Object FullName
``` 

- Look for package manifests and lockfiles: `package.json`, `yarn.lock`, `pnpm-lock.yaml`, `pyproject.toml`, `requirements.txt`, `Pipfile`, `setup.py`, `go.mod`, `pom.xml`, `build.gradle`.
- Look for CI/workflow files: `.github/workflows/**` and `docker-compose.yml`, `Dockerfile`.
- If a `README.md` exists, read it for project goals and run steps.

2) Big-picture signals to infer architecture
- Presence of `package.json` and `src/` often indicates a Node.js monorepo or single-package repo.
- `services/` or `api/` + `docker-compose.yml` implies multi-service architecture; treat folders under `services/` as service boundaries.
- `pyproject.toml` / `src/` with `tests/` suggests a Python package; examine `tool.poetry` or `setuptools` fields to determine packaging and entry points.
- Monorepo indicators: `workspaces` in `package.json`, `pnpm-workspace.yaml`, `packages/` directory.

3) Critical developer workflows (what to run/expect)
- If `package.json` exists: run `npm ci` or `npm install` then `npm test` or `npm run build` depending on scripts.
- If `pyproject.toml` with Poetry: `poetry install` then `poetry run pytest`.
- If `Makefile` exists, inspect `make test` and `make build` targets.
- If GitHub Actions present, open workflow YAMLs to see test matrix, required environment variables, or secrets.

4) Project-specific patterns to look for
- Check for a `src/` directory vs. top-level packages — the project prefers `src/` layout if present.
- Tests in `tests/` or `__tests__/` — follow their naming conventions for new tests.
- Linting/formatting: presence of `.eslintrc`, `.prettierrc`, `pyproject.toml` formatting settings; follow those config files rather than inserting new styles.

5) Integration points & external dependencies
- Look for environment file patterns: `.env.example`, `env.sample`, or GitHub Secrets referenced in `.github/workflows`.
- External services may be described in `docker-compose.yml`, `.devcontainer`, or README; follow those for local end-to-end runs.

6) How to modify the repo safely
- If repo has CI, mirror CI commands locally first and reproduce failures before changing configs.
- Add minimal, focused commits with a short description of the intent (e.g., `chore: add copilot instructions`).

7) Examples & quick templates (when creating new code)
- If adding a Node script, place under `src/` and expose an npm script in `package.json`:
  - "build": "tsc -p tsconfig.json" or "build": "webpack --config webpack.config.js" depending on existing tooling.
- If adding a Python package, ensure `src/<package_name>/__init__.py` exists and add tests under `tests/` matching existing patterns.

8) When you cannot discover anything
- Ask the user for the project's language, primary entry point, and intended runtime (e.g., "Is this a Node, Python, or mixed repo?").
- If the repository is intentionally empty (starter repo), propose a minimal scaffold matching the user's stated stack.

9) Communication & safety
- Reference the exact files you changed in the PR description and the commands you ran to validate changes.
- Avoid making high-risk changes (CI, release configs, secret handling) without explicit confirmation.

If any of the above steps found specific files or commands in this repository, insert them here and re-run discovery. Ask the repo owner for missing details: primary language, how to run tests locally, and whether there are required environment variables or external services.

---
Please review and tell me any project-specific files, typical commands, or patterns I should include (for example: the `package.json` script to run tests, a `docker-compose.yml` service name, or the primary package directory). I will merge them into this file and tighten the instructions.