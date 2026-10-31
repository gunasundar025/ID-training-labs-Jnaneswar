# Python Learning Labs

A hands-on path from Python basics to an advanced, testable final project. Each learner completes one lab at a time and opens a pull request (PR) into `dev` for review.

## Learning path

| Lab | Topics | Deliverable |
| --- | --- | --- |
| 01 | Setup, values, variables, input/output, type conversion | Unit converter CLI |
| 02 | Conditions, loops, validation | Number guessing game |
| 03 | Functions, parameters, return values, scope | Reusable calculator |
| 04 | Lists, dictionaries, sets, comprehensions | Contact book operations |
| 05 | Files, JSON, exceptions, paths | Persistent notes manager |
| 06 | Classes, objects, dataclasses, encapsulation | Library checkout model |
| 07 | Imports, packages, unittest, logging | Tested command line package |
| 08 | Iterators, generators, decorators, context managers, typing | Streaming log analyzer |
| Final | Design, persistence, validation, tests, documentation | Personal Finance Tracker CLI |

Start with [Getting started](CONTRIBUTING.md), then read each lab's `README.md` and implement its starter module. The `tests/` directory contains starter acceptance tests. Tests describe expected behavior; learners should add their own cases too.

## Suggested pace

Complete one lab per PR. The reviewer should check the code, tests, and the learner's short explanation of their approach. Do not begin the next lab until the current PR is merged into `dev`.

## Repository layout

```text
python-learning-labs/
├── labs/                 # Lesson briefs and starter modules (lab_01_... through lab_08_...)
├── src/                  # Final project starter package
├── final_project/        # Project requirements and rubric
├── tests/                # Lab acceptance tests
├── CONTRIBUTING.md       # Setup and branch/PR workflow
└── pyproject.toml
```
