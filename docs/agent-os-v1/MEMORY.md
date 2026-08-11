# Agent OS V1 — Memory Policy

Agent OS V1 treats memory as an operational asset, not a transcript archive. Save information only when it is likely to improve a later mission.

## Store

### Project facts

Verified facts that remain relevant across sessions: project names, architectures, important resources, stable environments, ownership, and current operating state.

### Decisions

Decisions that constrain future work, including the selected approach and the reason it was chosen when that reason matters later.

### Constraints

Explicit requirements, compatibility boundaries, safety rules, budgets, platform requirements, deadlines, and other limits that future work must respect.

### Successful procedures

Repeatable steps that were verified to work: setup procedures, troubleshooting sequences, build/release routines, research methods, and tool combinations.

### Failures and lessons

Verified failures that are likely to recur, including the observed symptom, actual cause when known, and the correction that worked.

### User-approved preferences

Stable preferences that materially affect execution or output and are appropriate to retain.

## Do not store

- Passwords, API keys, access tokens, private keys, recovery codes, or other secrets.
- Unsupported guesses or conclusions presented as facts.
- Temporary intermediate reasoning that has no future operational value.
- Routine status chatter such as "starting task" or "search complete."
- Duplicate copies of raw logs when the useful lesson can be summarized safely.
- Large source documents merely because they were read; index or reference them through the appropriate OpenJarvis memory/document tooling instead.
- Sensitive information unless retaining it is necessary, authorized, and consistent with the configured storage/security policy.

## Memory entry format

Prefer compact entries that answer four questions:

1. **What is true or what was decided?**
2. **What evidence or event supports it?**
3. **Why will this matter later?**
4. **When should it be reconsidered or invalidated?**

Example:

```text
Decision: Agent OS V1 extends OpenJarvis instead of replacing its orchestrator.
Support: V1 uses the built-in orchestrator, memory, skills, tools, traces, and scheduler.
Future value: Keeps upstream merges manageable and avoids duplicate runtimes.
Revisit when: A later phase requires durable multi-process agent isolation that the built-in runtime cannot provide.
```

## Verification rule

A memory entry should not make a stronger claim than the mission evidence supports. When certainty is limited, record the limitation explicitly rather than converting an inference into a permanent fact.
