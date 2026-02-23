# Repository Guidelines

## Project Structure & Module Organization
`src/fund/` holds the Python package and CLI modules (entry point `fund.main:cli`). `source/` is the Sphinx source tree that the Makefile uses to build documentation into `build/html/`; `README.rst`, `README.md`, and `CHANGELOG.md` live at the root alongside config files (`config.yml`, `pyproject.toml`) so keep updates synchronized. Exploratory work belongs in `notebooks/`, scraped data and snapshots live in `data/`, and `tmp/` hosts ephemeral outputs. Auxiliary scripts such as `bin/fix_matplotlib.py`, `pipeline.sh`, and `push.sh` sit at the repo root to keep short-lived helpers easy to invoke.

## Build, Test, and Development Commands
- `mamba create -n fund python=3.8 && mamba activate fund`: replicates the documented Conda environment (use `mamba install`/`pip install -e .` immediately after to bring in dependencies).  
- `pip install -e . -i https://pypi.tuna.tsinghua.edu.cn/simple`: installs the package in editable mode so edits to `src/fund` reload instantly.  
- `fund crawl`, `fund analysis`, `fund track`, `fund record`: core CLI workflows for collecting data, analyzing funds, plotting positions, and recording trades; run them in that order or wrap them with `bash pipeline.sh`.  
- `bash pipeline.sh`: sequential shorthand for `fund crawl`, `analysis`, and `track`; keep it in sync when you add new CLI verbs.  
- `fund summary --code_id 010213`: generate a detailed JSON summary plus `strategy.json` for ChatGPT-based fund recommendations.  
- `make html`, `make serve`: build Sphinx HTML in `build/html` and serve it locally (or use `bash server.sh` to build + `python -m http.server 8000`).

## Coding Style & Naming Conventions
Follow Python 3.8 / PEP 8 conventions; prefer four-space indentation, descriptive function names (`crawl_funds`, `plot_track`), and module-level constants in `SCREAMING_SNAKE_CASE`. Keep CLI commands verbs-first (`fund crawl`, `fund analysis`), and house reusable helpers in `core.py`, `utils.py`, or separate modules under `src/fund/` rather than scattering logic across scripts.

## Testing Guidelines
There are no automated tests yet. When adding tests, place them under a new top-level `tests/` directory, name files `test_<module>.py`, and rely on `pytest` (run via `python -m pytest`). Aim for one test file per feature, include fixtures next to the data they assert on, and update `README`/`docs` with new coverage expectations.

## Commit & Pull Request Guidelines
Commitizen governs commit messages: stick to Conventional Commits (`feat:`, `fix:`, `docs:`, `bump:`, etc.) and include scope when helpful (`fix(core): …`). PRs should explain the change, link related issues (or state “no issue”), summarize testing performed, and attach screenshots only for UI outputs (plots, notebooks). Mention any local scripts you ran (`bash pipeline.sh`, `fund record`) so reviewers can reproduce the workflow.
