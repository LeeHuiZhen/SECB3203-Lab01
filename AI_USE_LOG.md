# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 1
- Student name: Lee Hui Zhen
- Matric no: A24CS0259
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 22 October 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 22 October 2026, 4:50 PM
- Tool: Google (2026). Gemini. Retrieved 22 October 2026 from https://gemini.google.com
- Purpose: debug
- Prompt: "The system cannot find the path specified when running .venv\Scripts\activate.bat in Windows terminal"
- Output: Advised checking `where python` to confirm the interpreter path, noting that an incomplete environment creation or using a non-Windows native Python binary can cause missing activate scripts.
- Verified by: Inspected the `.venv/Scripts` directory in Command Prompt and recreated the virtual environment using the direct Python 3.14 path.
- My change: Followed the recommendation to rerun `python -m venv .venv` and successfully activated it using `activate.bat`.
- Used in: Virtual environment setup (.venv).

## Entry 2

- Date: 22 October 2026, 5:15 PM
- Tool: Google (2026). Gemini. Retrieved 22 October 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "Why do starter files have raise NotImplementedError in functions like package_version and gc_percent?"
- Output: Explained that `raise NotImplementedError` serves as a placeholder stub that defines the function signature, and it must be replaced with the actual implementation so that tests do not fail.
- Verified by: Checked the Lab 1 brief instructions and Week 1 lecture slides regarding function contracts.
- My change: Kept the starter function signatures unchanged and filled in the implementation logic.
- Used in: `src/env_check.py` and `src/basics.py`.

## Entry 3

- Date: 22 October 2026, 5:30 PM
- Tool: Google (2026). Gemini. Retrieved 22 October 2026 from https://gemini.google.com
- Purpose: tests-plan
- Prompt: "What kind of test cases should I include to test gc_percent and parse_counts for boundary and invalid values?"
- Output: Suggested testing extreme inputs (such as 100% G/C counts for boundary), a zero-sum count raising `ValueError`, and formatting errors like negative numbers or incorrect count lengths in strings.
- Verified by: Checked against rubric criteria R2, R3, and R6 for required edge cases.
- My change: Wrote three standalone test functions (`test_gc_percent_boundary_all_gc`, `test_gc_percent_zero_total_raises`, and `test_parse_counts_invalid_input_raises`) using `pytest.approx` and `pytest.raises`.
- Used in: `tests/test_lab01_own.py`.

## Entry 4

- Date: 22 October 2026, 5:45 PM
- Tool: Google (2026). Gemini. Retrieved 22 October 2026 from https://gemini.google.com
- Purpose: debug
- Prompt: "ruff check gives I001 Import block is un-sorted or un-formatted on tests/test_lab01_own.py"
- Output: Pointed out that PEP 8 requires standard/third-party imports (`pytest`) to be separated from local application imports (`basics`) by a blank line.
- Verified by: Ran `ruff check src tests` in the terminal to verify the warning was resolved.
- My change: Added an empty line between `import pytest` and `from basics import ...`.
- Used in: `tests/test_lab01_own.py`.

## Entry 5

- Date: 22 October 2026, 6:05 PM
- Tool: Google (2026). Gemini. Retrieved 22 October 2026 from https://gemini.google.com
- Purpose: debug
- Prompt: "Running python -m pytest gives ModuleNotFoundError: No module named 'basics' when running from the parent folder"
- Output: Explained that running pytest outside the `lab01` root prevents pytest from finding `pytest.ini`, which defines `pythonpath = src`.
- Verified by: Checked current working directory with `pwd`/`cd` and verified the location of `pytest.ini`.
- My change: Changed directory into `lab01` before running `pytest` and `ruff check`.
- Used in: Terminal test execution.