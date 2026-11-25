---
name: verify-change
description: Verify code changes before completing a task or preparing a pull request.
owner: "@IraOets"
why: "Ensure AI-generated changes are tested, reviewed, and safe."
review-by: "2027-01-20"
---

# Verify Change

Use this skill after modifying code and before reporting that a task is complete.

## Steps

1. Run `git diff` to inspect all code changes.
2. Check for unintended modifications or exposed secrets.
3. Run `npm run lint` if the command is available.
4. Run relevant tests using the scripts defined in `package.json`.
5. Run `npm run build` if the command is available.
6. Verify that API changes follow `.claude/rules/api.md`.
7. Report any failed or unavailable checks.

## Completion Checklist

- [ ] Changes match the requested task.
- [ ] No secrets or unrelated files were modified.
- [ ] Relevant checks passed or failures were documented.
- [ ] The final summary lists changed files and verification results.