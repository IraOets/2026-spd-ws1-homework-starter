# Agent Instructions

## Project
This repository is a training project for building a governed AI team harness.

## Working Rules
- Read `docs/ai/team-agreement.md` before making changes.
- Follow path-specific rules in `.claude/rules/`.
- Use relevant skills from `.claude/skills/`.
- Never access or expose secrets.
- Do not modify database migrations without human approval.
- Do not commit or push changes without explicit approval.

## Validation
- Run `npm run lint` when available.
- Run relevant tests before completing a task.
- Review the diff for unintended changes.
- Report any failed or unavailable checks.

## Handoff
- Summarize changes and verification results.
- Use `docs/ai/handoff-template.md` when handing off unfinished work.