# Team AI agreement — <team name>

<!-- owner: @<github-handle> · review-by: <YYYY-MM-DD> · change it by PR, CODEOWNERS approve -->

This agreement defines how AI agents can modify the repository, what checks are required, and who is responsible for their work.

## 1. Autonomy matrix

Levels: **L0** no agent · **L1** agent suggests, human writes · **L2** agent writes, human reviews every line ·
**L3** agent writes and runs checks, human reviews the PR · **L4** agent merges when gates are green, human audits samples.

| Change type | Level | Evidence that earns this level | Who signs off |
|---|---|---|---|
| Documentation changes | L3| Markdown validation passes; links and diff reviewed | PR author / reviewer |
| UI components | L3 | Lint, tests and build pass; UI changes manually reviewed | PR reviewer |
| API endpoints | L2 | API tests pass; input validation and error handling reviewed | PR reviewer |
| Database migrations | L2 | Migration tested on a fresh database; rollback procedure documented | Repository owner|
| Editing applied migrations       | L0     | Changes prohibited and blocked by a hook                               | -             |

Rule of thumb: A change type may receive more autonomy only when its verification is repeatable, reliable, and independent of the agent.

## 2. Who owns agent output

The person opening the PR is responsible for all AI-generated changes as if they wrote the code themselves.

AI-generated changes must be reviewed and tested before merging.

## 3. Harness owners

`AGENTS.md`: @IraOets

`.claude/**`: @IraOets

`docs/ai/**`: @IraOets

Ownership is enforced through `.github/CODEOWNERS`.

## 4. How rules change

1. Any contributor may propose a rule change through a Pull Request.
2. The harness owner reviews the change and its justification.
3. Behaviour-changing rules require evidence, such as an A/B comparison or hook test.
4. Changes are merged only after approval from the responsible CODEOWNER.
5. Rules must be reviewed by their review-by date and updated, renewed, or removed.

## 5. Personal vs team

Personal preferences: `~/.claude/CLAUDE.md`, `.claude/settings.local.json` (git-ignored).
Repository-level rules must be committed and shared with the team.
Do not commit `CLAUDE.md` / `CLAUDE.local.md` in the repo.
