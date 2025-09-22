# IndexedLinkedList

A Python data structure that combines characteristics of a linked list with O(1) index addressing via an internal index-to-UUID map. This allows you to:

- Add values and receive a stable integer index back
- Access values by index in O(1)
- Retrieve first/last values efficiently
- Convert to common Python containers (dict, list, set, tuple)
- Optionally enable strict mode to raise errors on invalid indices/values

The core implementation lives in `src/indexedlinkedlist/core/core.py` and is surfaced as `IndexedLinkedList` via `src/indexedlinkedlist/__init__.py`.

## Installation

This project is laid out as a standard Python package under `src/`. Until a distribution is published, install it from source:

```bash
git clone https://github.com/louisgoodnews/IndexedLinkedList.git
cd IndexedLinkedList
pip install -e .
```

This uses your active Python environment. You can also use a virtual environment of your choice before installing.

## Quick Start

```python
from indexedlinkedlist import IndexedLinkedList

# Create a list (non-strict by default)
ll = IndexedLinkedList()

# Add items -> returns the assigned index
i0 = ll.add("alpha")   # e.g. 0
i1 = ll.add("beta")    # e.g. 1

# Index access
print(ll[i0])  # "alpha"
print(ll[i1])  # "beta"

# Update by index
ll[i1] = "beta+"

# Query helpers
print(ll.get_first())  # first value or None
print(ll.get_last())   # last value or None
print(ll.index_of("alpha"))  # index of value or None

# Conversions
print(ll.to_list())   # ["alpha", "beta+"]
print(ll.to_dict())   # {0: "alpha", 1: "beta+"}
print(ll.to_set())    # {"alpha", "beta+"}
print(ll.to_tuple())  # ("alpha", "beta+")

# Remove by index
ll.remove(i0)
```

## Strict Mode

`IndexedLinkedList(strict=True)` enables defensive checks:

- Invalid index access/updates raise `IndexError`
- Looking up the index of a value that is not present raises `ValueError`

Example:

```python
ll = IndexedLinkedList(strict=True)
ll.add("x")

# Raises IndexError if index is not present
try:
    _ = ll[999]
except IndexError as e:
    print(e)

# Raises ValueError if value is not present
try:
    ll.index_of("missing")
except ValueError as e:
    print(e)
```

## API Overview

Public class: `indexedlinkedlist.IndexedLinkedList`

- `__init__(strict: bool = False, *args)`
  - Create a new list. If extra values are provided in `*args`, they are added in order.

- `add(value) -> int`
  - Append a value and return its assigned index.

- `__getitem__(index: int) -> Any`
  - Retrieve the value at `index`. Returns `None` in non-strict mode if `index` is absent; raises `IndexError` in strict mode.

- `__setitem__(index: int, value: Any) -> None`
  - Update the value at `index`. In strict mode, raises `IndexError` when `index` is absent.

- `__len__() -> int` or `size` property
  - Number of indexed positions in the storage (includes potential gaps if items have been removed).

- `get_first() -> Optional[Any]`
  - First present value or `None`.

- `get_last() -> Optional[Any]`
  - Last present value or `None`.

- `index_of(value: Any) -> Optional[int]`
  - Index of `value` if present or `None`. In strict mode, raises `ValueError` when value is not present.

- `remove(index: int) -> None`
  - Remove value at `index`. The slot becomes unused; future `add` calls may reuse the earliest available unused slot.

- `update(index: int, value: Any) -> bool`
  - Update value by index. Returns `True` if updated, `False` otherwise. In strict mode, invalid indices raise `IndexError`.

- `to_dict() -> dict[int, Any]`
  - Snapshot mapping from sequential enumeration of `to_list()` to values.

- `to_list() -> list[Any]`
  - Snapshot list of current values in storage order.

- `to_set() -> set[Any]`, `to_tuple() -> tuple[Any]`
  - Convenience conversions based on `to_list()`.

Notes:
- The underlying storage is managed by `IndexedLinkedNodeStorage` which tracks a head, tail, and two mappings:
  - `index -> uuid` and `uuid -> node`
- Removal sets entries to `None` internally; methods like `get_first()`/`get_last()` skip over unused indices.

## Behavior and Complexity

- `add` is amortized O(1)
- `__getitem__` and `__setitem__` are O(1)
- `index_of(value)` is O(n) in the number of present nodes
- Conversion helpers are O(n)

## Examples

Minimal usage example is provided above. You can also initialize with values directly:

```python
ll = IndexedLinkedList(False, "a", "b", "c")
print(ll.to_list())  # ["a", "b", "c"]
```

## Development

- Python version: modern type-annotated code (PEP 563/PEP 649-ready); ensure Python 3.11+ recommended
- Run tests (if/when added) using your preferred runner, e.g. `pytest`
- Lint/format using the settings in `setup.cfg` (if configured)

## Project Structure

- `src/indexedlinkedlist/core/core.py`: core implementation of nodes, storage, and the public `IndexedLinkedList`
- `src/indexedlinkedlist/__init__.py`: exports `IndexedLinkedList`, defines `__version__`
- `src/indexedlinkedlist/utils/utils.py`: small utility (e.g., `invert_dict`)
- `examples/`: example placeholders
- `tests/`: test placeholders

## License

This project is licensed under the MIT License. See `LICENSE` for details.
