# Upstream review

Reviewed on 2026-10-14 for this toolkit snapshot. This is a scoped static review,
not an independent security audit, legal opinion or guarantee of model behavior.
Exact source commits, directory mappings and file checksums are recorded in
`upstream-lock.json`. No upstream installers, hooks or package managers were run.

## Sources and licensing

- `wondelai/skills`: root MIT license, copyright 2025 Wondel.ai sp. z o.o.;
  copied create-business and its ten core framework directories with their local
  references. Each skill declares MIT in frontmatter. No plugins or repository
  automation were imported.
- `phuryn/pm-skills`: root MIT license, copyright 2026 Pawel Huryn; copied only
  `pm-product-strategy/skills/business-model`. Its source is the actual author's
  repository, rather than the third-party listing in the earlier conversation.
- `magnus919/agent-skills`: root `LICENSE.md` is MIT, copyright 2026 Magnus
  Hedemark; financial-modeling also declares MIT. Copied its directory, including
  templates, references, eval manifest, calculator and calculator tests. Its
  source-index records earlier provenance from `magnus919/hermes-profiles` at
  `867a555`; that historical source-index is retained unchanged. This toolkit's
  lock identifies the full commit actually copied from agent-skills.

License notices were checked before vendoring and copied into every skill folder.
No conflicting license was found in the copied directory trees. Upstream skill
files remain byte-for-byte unchanged; added LICENSE files are separately mapped
in the lock. Root documentation/code has a separate MIT license. The included
framework summaries refer to books and commercial frameworks; the upstream MIT
grant is not a grant to reproduce those books or their third-party assets.

## Review scope and findings

- Inventoried every imported file and scanned Markdown for remote commands,
  execution directives, secrets/access requests, uploads and instruction overrides.
  Reviewed the core entrypoints and relevant flagged passages. Files are Markdown,
  JSON and two Python files; no binaries, symlinks, hooks, hidden installers or
  package dependencies are imported. Checksums cover every imported file.
- The create-business entrypoint suggests an unpinned global `npx skills add`
  fallback. All ten core skills are bundled, and AGENTS.md directs agents to use
  those copies. Optional skills are not automatically installed. Original command
  text is retained for provenance, not approved for execution.
- Wondelai's entrypoints include Amazon links with affiliate parameters. These
  are retained and disclosed; purchases are unnecessary. Some sprint references
  discuss uploading sketches to collaboration services. Such methodological
  examples do not authorize uploads of founder/customer data.
- The journey has frequent sign-off prompts, fixed interview counts and evidence
  gates. The toolkit distinguishes an explicitly requested provisional draft from
  real validation. Evidence status stays pending even when drafts are finished.
- The business-model skill suggests LTV > 3× CAC as a test. AGENTS.md treats this
  as a contextual heuristic and requires explicit definitions and actual cash
  analysis rather than declaring viability from a ratio.
- The financial calculator imports only Python standard-library argparse, json
  and sys. It has no network access, file writes, shell execution or credential
  access. Its tests invoke that local calculator using the current Python
  interpreter, capture output and enforce a timeout; they do not invoke a shell.
  The JSON eval manifest is a set of prompts/expected outputs, not executable code.
- Calculator limitations: human-readable output hardcodes a dollar symbol; use
  `--json` and label currency separately for other currencies. It does not reject
  every non-finite numeric input or inconsistent combination of revenue movements.
  Supply finite, reconciled inputs and independently check the outputs. It is a
  convenience calculator, not a validated accounting system or forecast engine.
- Historical book case studies and financial benchmarks are teaching material,
  not current market evidence. The workflow requires current primary-source
  research, dated claims, separate assumptions and explicit tool/data limitations.
- No credential-exfiltration or malicious instruction-override directive was
  identified within this review scope. Prompt-based workflows still depend on
  the host's controls and the agent's judgment; this is not a sandbox.

## Validation and updates

Run `python3 scripts/verify_toolkit.py` for hashes, complete vendor inventory,
entrypoint names, licenses and local Markdown references. Run the bundled
`python3 .agents/skills/financial-modeling/scripts/test_saas_metrics.py` for its
calculator behavior checks. These do not constitute full end-to-end business-plan
evaluation, live market verification or a guarantee that every formula is suitable
for a particular venture. No real customer data is needed for these checks.

For an update: select a full commit, inspect that commit's license and the exact
changed files, review new executables/instructions and dependencies, then copy
only the intended directories. Preserve notices, regenerate the lock from the
reviewed files and record the changed scope/findings here. Run verification and
the calculator checks again. Never fetch an unreviewed latest version at runtime.

### Snapshot validation results

- All 13 skills passed the skill-creator frontmatter/structure validator.
- All 116 vendored files matched the lock and all local Markdown references resolved.
- All 21 upstream calculator tests passed.
- A separate temporary-copy check confirmed that altered skill content makes the
  integrity checker fail. No evaluation artifacts or validation dependencies are
  included in the repository.
- The staged changes passed Git's whitespace check. No live venture or end-to-end
  business-plan exercise was performed.
