# Business Planning Toolkit

An agent skill toolkit for turning an idea into an evidence-led business model,
market assessment, financial model and business plan. Use it with Codex or another
agent that can read local Markdown skills. No API keys, paid service, or package
installation is required by the toolkit itself. Research and spreadsheet tools
come from your agent environment.

## Setup

```sh
git clone https://github.com/AmirAbaris/business-planning-toolkit.git
cd business-planning-toolkit
python3 scripts/verify_toolkit.py
```

The repository is private by default, so cloning requires GitHub access. Open the
repository as your agent's working folder. Codex uses the root `AGENTS.md` and
project skills in `.agents/skills/`. For other agents, explicitly ask it to read
`AGENTS.md`, then load the relevant `.agents/skills/<name>/SKILL.md` and linked
references. Keep the whole folder structure together; host discovery behavior varies.
Python 3.9+ is needed only for the integrity checker and optional financial helper.
Nothing is installed globally and no upstream code runs during setup.

## Start a project

```text
Read AGENTS.md and use the bundled skills to assess this business idea:
[idea]. The customer is [segment] in [geography].
We have [evidence or “none yet”], a budget of [amount/currency], and [runway].
Prepare a [founder/investor/lender/partner] plan by [date].
Ask for missing decisions, label assumptions, and save the work locally.
```

For a quick first pass:

```text
Draft a provisional business model and a concise business plan for [idea].
Use explicit assumptions wherever evidence is missing. Identify the three
riskiest assumptions and design the cheapest experiments to test them.
```

To resume:

```text
Read docs/STATUS.md and the existing artifacts. Here are new customer notes:
[notes]. Update the evidence, model and plan; explain which conclusions changed.
```

You can also request one component: “Use business-model to build the nine-block
canvas,” or “Use financial-modeling to review my cash forecast.” In hosts with
named skill invocation, use their normal syntax (for example `$business-model`).
No customers, financial forecasts, or business-plan results are pre-populated.

## What's included

| Skill | Source | Purpose |
| --- | --- | --- |
| create-business | [wondelai/skills](https://github.com/wondelai/skills/tree/main/create-business) | Guided validation, positioning and pricing journey |
| business-model | [phuryn/pm-skills](https://github.com/phuryn/pm-skills/tree/main/pm-product-strategy/skills/business-model) | Nine-block Business Model Canvas |
| financial-modeling | [magnus919/agent-skills](https://github.com/magnus919/agent-skills/tree/main/financial-modeling) | Driver-based forecasts, pricing, unit economics and scenarios |

The ten core create-business dependencies are also included: jobs-to-be-done,
mom-test, design-sprint, lean-startup, good-strategy-bad-strategy,
blue-ocean-strategy, obviously-awesome, hundred-million-offers,
monetizing-innovation and crossing-the-chasm. All relevant local references are
bundled. Optional downstream journeys are not bundled or automatically installed.
Market research and business-plan synthesis are specified in `AGENTS.md`.

## Deliverables

The workflow creates `docs/` for the customer evidence, experiments, canvas,
market research, source/assumption registers, strategy, pricing, model notes,
milestones and resumable status. Final Markdown plans and an XLSX or transparent
CSV financial model go in `deliverables/`. An XLSX requires suitable spreadsheet
tools; unsupported exports and unverified formulas must be disclosed. These two
folders are ignored by Git to keep business data out of routine commits. Use a
separate clone for each venture; deliberately review any files you choose to share.

## Provenance, safety and maintenance

All 13 skills are MIT-licensed upstream snapshots, with license notices in every
skill folder. Exact commits, source paths and per-file SHA-256 checksums are in
`upstream-lock.json`; attribution is in `THIRD_PARTY_NOTICES.md`. Skill contents
are unchanged except for added copies of upstream license files. The root workflow
explains how to apply their methods within this toolkit.

See `docs-toolkit/UPSTREAM-REVIEW.md` for review scope, findings, limitations and
update procedure. The toolkit does not auto-update, run installers, contact
customers or upload documents. The optional financial helper is a local Python
calculator, not the full forecasting engine. Integrity checks detect snapshot
changes; they do not certify future agent behavior or business viability.

Original toolkit documentation and verification code use the root MIT `LICENSE`.
Upstream authors retain their copyrights. Framework and book names belong to
their respective authors/owners; inclusion implies no endorsement.
