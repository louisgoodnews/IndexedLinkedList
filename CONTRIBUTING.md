# Contributing to IndexedLinkedList

Thanks for your interest in contributing! This guide explains how to set up your environment, make changes, run checks, and submit pull requests.

## Code of Conduct

Participation in this project is governed by our Code of Conduct. Please read it before contributing.

- See: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## Getting Started

1. Fork the repository and create a feature branch
2. Clone your fork and enter the project directory

```bash
git clone https://github.com/louisgoodnews/IndexedLinkedList.git
cd IndexedLinkedList
```

3. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\\Scripts\\activate  # Windows PowerShell
```

4. Install in editable mode

```bash
pip install -e .
```

## Project Layout

- Source code: `src/indexedlinkedlist/`
  - Core: `src/indexedlinkedlist/core/core.py` (exports `IndexedLinkedList`)
  - Utils: `src/indexedlinkedlist/utils/utils.py`
- Examples: `examples/`
- Tests: `tests/`

## Running Tests

We recommend pytest.

```bash
pytest -q
```

With coverage (if configured):

```bash
pytest --maxfail=1 --disable-warnings -q --cov=indexedlinkedlist --cov-report=term-missing
```

## Linting and Formatting

If pre-commit is configured, you can install and run it:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

Common tools you may use (depending on project config):

- flake8 or ruff for linting
- black for formatting
- isort for import sorting

## Tox (optional)

If `tox.ini` is present, you can run multiple environments:

```bash
tox
```

## Making Changes

- Keep changes focused and incremental
- Add or update unit tests in `tests/` as needed
- Update documentation (docstrings, README) when behavior changes
- Maintain type hints and clear naming

### Commit Messages

- Use clear, descriptive messages
- Reference issues where applicable (e.g., `Fixes #123`, `Refs #456`)

### Branching

- Branch from the default branch (e.g., `main`)
- Example branch names: `feat/reuse-unused-index`, `fix/index-error`

## Pull Request Process

1. Ensure your branch is up to date with the default branch
2. Verify tests pass and code is linted/formatted
3. Open a PR with a clear title and description
4. Link related issues and describe rationale, approach, and any trade-offs
5. Address review feedback promptly

## Design and Performance Notes

This library provides an indexed linked list abstraction with:

- O(1) index addressing using internal `index -> uuid` and `uuid -> node` maps
- Efficient `get_first()` / `get_last()` that skip unused indices
- Optional strict mode for defensive error handling

Please preserve these characteristics and document any changes that affect complexity or behavior.

## Security

If you discover a security issue, do not open a public issue. Please contact the maintainers at:

- louisgoodnews95@gmail.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

- See: [LICENSE](LICENSE)
