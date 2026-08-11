# Agent OS V1 — Starter Missions

These templates are original operating patterns for the Agent OS V1 role contracts. Replace bracketed text with the actual objective and constraints. They are designed to run through the existing OpenJarvis orchestrator rather than a separate workflow engine.

## 1. Deep Research

### Objective

Research **[question/topic]** and produce an evidence-backed answer suitable for **[decision/use]**.

### Roles

- Commander: define the research question and success criteria.
- Researcher: gather and reconcile evidence.
- Verifier: check source support, contradictions, and unsupported claims.
- Memory Keeper: retain only durable conclusions and source-independent lessons.

### Execution

1. Break the question into the smallest material sub-questions.
2. Search relevant local documents, indexed memory, web sources, or connected data that are actually available.
3. Separate direct evidence, source claims, and inference.
4. Resolve meaningful conflicts when possible; otherwise preserve the disagreement.
5. Produce the decision-focused synthesis.

### Verification

Confirm that important factual claims are supported, uncertainties are visible, and citations or source references actually match the claims they support.

### Output

- Answer first
- Key evidence
- Material uncertainty/disagreement
- Recommendation or implication
- Durable lessons worth saving

---

## 2. Build

### Objective

Build or modify **[software/file/system/artifact]** so that it satisfies **[acceptance criteria]**.

### Roles

- Commander: define scope and dependency order.
- Researcher: inspect existing architecture/docs when needed.
- Builder: implement the change.
- Operator: run authorized tools, builds, or environment actions.
- Verifier: execute focused checks and inspect the resulting artifact.
- Memory Keeper: retain architecture decisions and verified procedures.

### Execution

1. Inspect the existing target before editing.
2. Identify the smallest observable slice that proves the requested behavior.
3. Add a focused failing check when the change is testable.
4. Implement the minimum coherent change.
5. Run narrow checks, then broader proportionate verification.
6. Review the diff/output for accidental unrelated changes.

### Verification

Require fresh evidence appropriate to the artifact: tests, lint/build output, deterministic inspection, or direct runtime behavior. Do not accept “generated successfully” as sufficient proof.

### Output

- What changed
- Files/resources affected
- Verification evidence
- Assumptions or limitations
- Next best action

---

## 3. Monitor

### Objective

Watch **[condition/source]** for **[meaningful change/threshold/event]** and surface only actionable changes.

### Roles

- Commander: define the condition and what counts as meaningful.
- Researcher: establish the baseline when required.
- Operator: use the available scheduler/continuous-agent tooling.
- Verifier: distinguish a real condition change from noise or missing data.
- Memory Keeper: retain the baseline and confirmed state transitions.

### Execution

1. Define the exact monitored condition and evidence needed to confirm it.
2. Record the current verified baseline.
3. Configure an appropriate schedule or continuous agent using existing OpenJarvis capabilities.
4. On each run, compare the new state to the baseline/last verified state.
5. Report only when the configured condition is satisfied or attention is required.

### Verification

Before alerting, confirm that the apparent change is not caused by stale data, a failed connector, missing coverage, or a parsing error.

### Output

- What changed
- Evidence and timestamp/context
- Why it matters
- Recommended action
- Updated durable baseline when appropriate

---

## 4. Business Ops

### Objective

Turn **[business problem/opportunity]** into a concrete, evidence-backed operating decision or deliverable.

### Roles

- Commander: define the business outcome and decision criteria.
- Researcher: gather relevant operational, market, customer, or financial evidence available to the system.
- Builder: produce the plan, model, process, document, or automation artifact.
- Operator: perform approved tool actions.
- Verifier: challenge assumptions, arithmetic, source quality, and implementation readiness.
- Memory Keeper: save durable operating decisions and procedures.

### Execution

1. State the decision to be made and the metric or outcome it should improve.
2. Gather only evidence that can materially change the decision.
3. Separate known numbers/facts from assumptions.
4. Produce the simplest actionable operating plan or artifact.
5. Identify dependencies, risks, and the first measurable checkpoint.

### Verification

Recalculate important numbers independently, check that assumptions are labeled, and verify that recommended actions follow from the evidence rather than from unsupported confidence.

### Output

- Decision/recommendation
- Evidence and assumptions
- Action sequence
- Risks/dependencies
- First measurable checkpoint

---

## 5. Daily Brief

### Objective

Convert **[today's/overnight/current]** available inputs into a short decision-oriented briefing.

### Roles

- Commander: prioritize what affects the user's day.
- Researcher: gather the configured calendar/messages/news/project inputs that are actually connected.
- Verifier: identify missing or stale sources and prevent them from being represented as complete coverage.
- Memory Keeper: save only durable decisions or commitments, not the entire brief.

### Execution

1. Gather the configured sources and note coverage gaps.
2. Remove duplicates and low-value noise.
3. Rank items by urgency, importance, and dependency.
4. Identify conflicts, deadlines, decisions, and useful free windows when those data are available.
5. Keep the brief concise enough to act on immediately.

### Verification

State source/coverage limitations when they matter. Confirm dates, times, and high-impact claims before presenting them as definite.

### Output

- Top priorities
- Decisions/risks
- Time-sensitive items
- Useful context
- Next actions
