# Final project: Personal Finance Tracker

Build a command line application that helps one user track income and expenses across runs.

## Required features

1. Add a transaction with date, description, amount, category, and type (income or expense).
2. Validate dates and positive amounts; reject unknown transaction types.
3. List transactions, filter by date range or category, and show totals by category.
4. Show the current balance (income minus expenses).
5. Persist data locally in JSON. Handle a missing data file and report invalid stored data clearly.
6. Provide a usable CLI with help text and clear error messages.
7. Separate domain logic, persistence, and CLI code. Use type hints and meaningful docstrings.
8. Add automated tests for core logic, validation, persistence, and CLI behavior where practical.

## Suggested milestones

- **Milestone 1:** define a transaction model and pure functions for totals and filtering.
- **Milestone 2:** add JSON persistence and tests using temporary directories.
- **Milestone 3:** build the CLI and validate user input.
- **Milestone 4:** add category summaries, documentation, and polish.

Create one PR per milestone, each targeting `dev`. The final PR should include setup and usage examples, design decisions, test command and results, known limitations, and a short demo transcript.

## Assessment rubric (100 points)

| Area | Points | Evidence |
| --- | ---: | --- |
| Correct features | 30 | Required actions and summaries work |
| Code design | 20 | Clear separation, readable names, appropriate functions/classes |
| Validation and errors | 15 | Invalid input and bad data handled safely |
| Tests | 20 | Useful coverage including edge cases |
| Usability and documentation | 10 | Clear CLI help and setup/usage instructions |
| Git workflow | 5 | Milestone PRs target `dev`; review feedback addressed |

## Stretch goals

CSV export, monthly reports, recurring transactions, configurable budgets, or a small database backend. Keep stretch work separate from the required features and test it.
