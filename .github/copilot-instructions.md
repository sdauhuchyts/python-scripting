# Copilot Instructions for python-scripting

## Project Overview

**Type**: Personal Python learning & practice repository  
**Focus**: Algorithm problems, file I/O, PCAP certification materials (Cisco Python exam prep)  
**Approach**: Exploratory—mix of single implementations and iterative solutions  
**Dependencies**: Standard library only (no external packages)

## Directory Structure

- **`exercises/`** — Algorithm challenges (string operations, intervals, list operations, Tinkoff coding competition problems)
- **`PCAP/`** — Core learning materials
  - `PCAP/modules/` — Module/import pattern examples
  - `PCAP/packages/` — Package structure examples
  - `PCAP/progs/` — Program variations showing different import approaches
  - `PCAP/*.py` — Utility programs (Caesar cipher, tic-tac-toe, sudoku, file I/O operations)

## Code Conventions

### Naming
- Descriptive, lowercase file names: `ceasar.py`, `day_of_year.py`, `tic-tac-toe.py`
- Multiple implementations of same problem: `tinkoff.py`, `tinkoff1.py` (iterative solutions)
- Private/internal functions use double underscore: `__counter`

### Style & Patterns
- **Dual-mode scripts**: Most files include `if __name__ == "__main__":` blocks
- **Error handling**: Try/except for user input validation (ValueError, IOError)
- **Performance awareness**: Comments note O(n) complexity; uses efficient algorithms
- **Idioms**: List comprehensions, string character encoding (ord/chr), context managers for file I/O
- **Comments**: Some in Russian (learning context)

### Functional Patterns
- **Multiple algorithm implementations**: Same problem solved 2+ ways within a file (e.g., `fun1()` vs `fun2()`)
- **Interactive programs**: Use `input()` for user interaction
- **File operations**: Read/write patterns with text test files (`text.txt`, `text_w.txt`)

## Running Code

All files are self-contained Python 3 scripts. Run individually:

```bash
python3 exercises/intervals.py
python3 PCAP/ceasar.py
python3 PCAP/tic-tac-toe.py
```

Interactive scripts prompt for user input. File-based programs expect data in `text.txt` or `text_w.txt`.

## Development Guidance

### When Adding New Code
- Keep algorithms self-contained in single files or one-file-per-concept
- Add `if __name__ == "__main__":` block for executable code
- Use descriptive function names: `calculate_day_of_year()` over `calc()`
- Include error handling for user input (ValueError, IOError)
- Comment non-obvious logic or performance considerations

### When Debugging/Refactoring
- Check both versions if multiple implementations exist (`fun1()`, `fun2()`)
- Validate file I/O assumptions (check `text.txt` exists and has expected format)
- Test interactive code with representative input
- Preserve existing function signatures if used as learning examples

### Common Pitfalls
- File operations may fail if `text.txt` is missing—check working directory
- Interactive scripts require manual input (cannot be automated without stdin)
- Module imports in `PCAP/modules/` are example patterns, not production code
- String encoding edge cases in Caesar cipher (handle wrapping correctly)

## Key Files & Patterns to Reference

| File | Pattern/Concept |
|------|-----------------|
| `exercises/list_intersection.py` | Algorithm optimization, list operations |
| `PCAP/ceasar.py` | Character encoding, input validation, encryption |
| `PCAP/tic-tac-toe.py` | Interactive game, state management |
| `PCAP/modules/module.py` | Module documentation, private attributes |
| `PCAP/file_readlines.py` | File I/O patterns, context managers |

## Notes for AI Agents

- ✅ Pure Python—no build system or setup required
- ✅ All scripts are standalone (can run independently)  
- ✅ Start with `exercises/` for algorithm patterns; check PCAP for file/module examples
- ✅ When modifying: preserve dual implementations and test both before/after versions
- ✅ Use standard library only; do not introduce external dependencies
