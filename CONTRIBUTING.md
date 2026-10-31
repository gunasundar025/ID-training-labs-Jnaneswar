# Learner setup and contribution workflow

## 1. Set up your environment

Use Python 3.11 or newer. Clone the repository, enter its directory, create a virtual environment, and install the project in editable mode:

```bash
git clone <repository-url>
cd python-learning-labs
git switch dev
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\activate` on Windows, then run:

```bash
python -m pip install -e .
```

## 2. One task, one branch, one PR

For each lab, start from the latest `dev` branch and create a short-lived branch:

```bash
git switch dev
git pull origin dev
git switch -c task/01-python-basics
```

Implement only that lab, run its acceptance tests, and commit your work:

```bash
python -m unittest discover -s tests -v
git add labs tests
git commit -m "Complete lab 01: Python basics"
git push -u origin task/01-python-basics
```

Open a PR with **base `dev`** and your task branch as the compare branch. Include:

- The lab number and a short summary.
- How you ran the code and tests, with results.
- One thing you learned and any question you have.

Ask for review, address feedback on the same branch, and wait for the PR to be approved and merged before starting the next lab. Do not push directly to `dev` or `main`.

Suggested branch names: `task/01-python-basics`, `task/02-control-flow`, and `project/final-finance-tracker`.

## Reviewer checklist

- The change meets the lab requirements and stays in scope.
- Names and structure are clear; input errors are handled where requested.
- Relevant tests pass and include meaningful edge cases.
- The PR explains the approach and test results.

## Maintainer setup

Create a `dev` branch on the hosting service and set it as the default collaboration branch. Protect `dev` and `main`: require PRs, at least one approval, and passing checks before merging; disable direct pushes. Learner PRs target `dev`. Promote a completed cohort or release from `dev` to `main` with a separate maintainer PR.
