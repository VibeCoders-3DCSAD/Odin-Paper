# Git Commit Message Standards

Shared across all BUDI repositories.

## Format

```text
<type>(<scope>): <brief message>

[optional body]

[optional footer]
```

- Use lowercase `type` and `scope` tokens.
- Always include a scope. Do not use unscoped subjects such as `fix: ...`.
- Keep the brief message specific, imperative, and focused on the change.

## Commit Types

| Type | Use For |
|------|---------|
| `build` | Build system, packaging, or compile pipeline changes |
| `chore` | Maintenance tasks that do not change functionality |
| `ci` | Continuous integration, checks, or release automation |
| `docs` | Documentation-only changes |
| `feat` | New features or capabilities |
| `fix` | Bug fixes or behavior corrections |
| `perf` | Performance improvements |
| `refactor` | Structural improvements without changing behavior |
| `revert` | Reverts of prior commits |
| `style` | Formatting-only changes with no behavior impact |
| `test` | Test-only changes |

## Commit Scopes (BUDI-Base)

| Scope | Use For |
|-------|---------|
| `model` | Model design documents and data analysis |
| `data` | Data sources, synthetic data, FIES/BSP files |
| `docs` | Thesis documents, specifications, chapter drafts |
| `survey` | Survey instruments and notes |
| `config` | Repo configuration, tooling, scripts |
| `standards` | Shared engineering standards and agent guidance |
| `deps` | Dependency additions, removals, upgrades |

> **Note:** RRL corpus commits (previously `rrl` scope) now belong in **BUDI-Literature**. BUDI-Base only tracks RRL-related documentation references.

Examples:

```text
docs(model): add RF classifier prep notes
chore(config): update .gitignore for __pycache__
```

## Subject Rules

- 50-72 characters when possible.
- Imperative mood.
- Lowercase unless it begins with a proper noun, acronym, or code identifier.
- No trailing period.

## Body Rules

- Blank line between subject and body.
- Wrap at 72 characters.
- Explain what changed and why.
- Prefer context over repeating diff details.

Suggested body order:

1. Current situation
2. Reason for change
3. Action taken
4. Impact or notes

## Footer Rules

- Use `Fixes:`, `Closes:`, `Refs:`, `See also:`, or `BREAKING CHANGE:`.
- Keep concise.

## Quality Rule

A valid commit subject completes this sentence:

```text
If applied, this commit will <your subject line here>
```
