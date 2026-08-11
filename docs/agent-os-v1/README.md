# Agent OS V1

Agent OS V1 is a starter operating layer for OpenJarvis. It keeps OpenJarvis as the engine and packages its existing orchestrator, tools, skills, memory, traces, scheduler, workflows, server/desktop surfaces, and local-first model stack around a simple rule: one objective comes in, work is planned by role, and nothing is called complete until it is verified.

This V1 is intentionally small and upstream-friendly. It does not add a second orchestration runtime.

## Quick start

Install OpenJarvis using the normal project instructions, then initialize the Agent OS preset:

```bash
jarvis init --preset agent-os-v1
jarvis doctor
```

Start your first mission:

```bash
jarvis ask "Objective: Research a topic, produce an evidence-backed recommendation, verify the claims, and save only durable lessons."
```

For a build mission:

```bash
jarvis ask "Objective: Inspect this project, implement the requested change with the smallest safe diff, verify it with fresh checks, and report exactly what changed."
```

## Operating model

The default preset uses OpenJarvis's existing `orchestrator` as Commander. It can use the installed tools and skills to perform work under six role contracts:

- Commander
- Researcher
- Builder
- Operator
- Verifier
- Memory Keeper

See [AGENTS.md](AGENTS.md) for the role contracts and handoff rules.

## Starter missions

Five reusable mission patterns are included:

1. Deep Research
2. Build
3. Monitor
4. Business Ops
5. Daily Brief

See [MISSIONS.md](MISSIONS.md) for the executable templates.

## Memory

The preset enables memory context and SQLite-backed storage. Agent OS V1 is deliberately selective about what becomes durable memory: verified project facts, decisions, constraints, successful procedures, recurring preferences, and lessons from confirmed failures.

See [MEMORY.md](MEMORY.md) for the retention policy.

## Existing OpenJarvis capabilities to use with V1

### Server and desktop surfaces

Start the existing OpenJarvis API server when you want the browser/desktop client to connect to the Agent OS configuration:

```bash
jarvis serve
```

OpenJarvis also ships a desktop GUI through its normal release/install path. Agent OS V1 reuses those surfaces rather than adding a separate command-center application in this phase.

The repository contains a terminal dashboard component as well, but V1 does not invent a CLI command for it when the current upstream command registry does not expose one.

### Skills

Inspect and install skills through the existing skill system:

```bash
jarvis skill --help
jarvis skill install hermes:arxiv
```

Only install skills from sources you trust. A skill can expand what an agent is able to do with tools and data.

### Memory and local documents

Use the existing memory commands to index or inspect information that should be available to missions:

```bash
jarvis memory --help
```

Keep raw documents in the appropriate indexed/document store; do not turn `MEMORY.md` into a dump of entire source files.

### Scheduling and monitoring

Use the existing scheduler for recurring work:

```bash
jarvis scheduler --help
```

The Monitor mission template in [MISSIONS.md](MISSIONS.md) defines the operating rules for meaningful-change monitoring and verification.

### Models

Agent OS V1 defaults to Ollama with `qwen3.5:9b`, following the same model family used by other OpenJarvis starter presets. Change the model or engine using normal OpenJarvis configuration if another local or cloud model is more appropriate for your hardware and task.

## Default security posture

The V1 preset binds the server to loopback:

```toml
[server]
host = "127.0.0.1"
```

It also reuses OpenJarvis's own security/privacy tooling rather than creating a second policy engine. Run:

```bash
jarvis doctor
jarvis scan
```

before granting additional tool access or exposing services beyond the local machine.

## What comes later

V1 deliberately does not include a new wake-word/voice pipeline, a dedicated process per role, a mission DAG database, a new approval engine, a knowledge graph, autonomous skill generation, or a custom futuristic command-center redesign. Those are later JARVIS layers after this baseline is stable.
