# Agent OS V1 Design

## Goal

Create a practical starter Agent OS on top of OpenJarvis without replacing its core architecture. V1 must be immediately usable as an OpenJarvis preset and package a coordinated agent operating model around the existing orchestrator, memory, skills, tools, scheduler, workflows, dashboard, and local/cloud model routing.

## Design principles

1. **Preserve upstream compatibility.** Prefer additive files and tiny, isolated changes to core OpenJarvis code so future upstream merges remain manageable.
2. **Use existing primitives first.** Reuse the built-in orchestrator, tools, memory, skills, scheduler, workflow engine, dashboard, traces, and security defaults instead of duplicating them.
3. **Starter product, not a demo.** V1 should give a new user one preset, one operating doctrine, five starter mission templates, and six clear agent roles.
4. **Verification before completion.** Mission instructions require a verifier pass before a result is declared complete.
5. **Local-first by default.** Keep OpenJarvis local-first behavior and permit cloud escalation through existing provider/model configuration.
6. **No proprietary copying.** Do not include paid third-party prompts, course text, private workflows, branding, or other protected material. Recreate only general agent-OS concepts using original implementation and wording.

## V1 architecture

### OpenJarvis core retained

- Intelligence/model routing
- Agent runtime and orchestrator
- Tool registry and MCP support
- Memory and trace storage
- Skills catalog/import system
- Scheduler and continuous agents
- Workflow command support
- Existing dashboard and desktop application
- Security/privacy checks

### Agent OS layer added

The Agent OS layer is primarily configuration, operating doctrine, role definitions, mission templates, and onboarding. It does not introduce a parallel orchestration engine.

The default V1 team is:

- **Commander** — owns the objective, decomposes work, assigns roles, tracks completion criteria, and returns the final answer.
- **Researcher** — gathers and organizes evidence from web, local documents, and connected sources.
- **Builder** — creates code, files, analyses, or other implementation artifacts.
- **Operator** — performs approved tool and computer actions using the capabilities exposed by OpenJarvis.
- **Verifier** — checks outputs against the objective, evidence, tests, and explicit acceptance criteria.
- **Memory Keeper** — records durable project facts, decisions, constraints, lessons, and successful procedures.

In V1 these are role contracts used by the orchestrator rather than six permanently running processes. This keeps V1 simple while preserving a path to dedicated agent processes later.

## Data flow

1. User supplies an objective.
2. The orchestrator acts as Commander and creates a concise task plan.
3. It assigns each task one of the role contracts above.
4. Agents use existing OpenJarvis tools, skills, memory, and model routing.
5. Builder/Operator outputs are passed through Verifier criteria before completion.
6. Memory Keeper rules determine which durable facts and lessons should be saved.
7. Commander returns the result with completed work, unresolved blockers, and next recommended action.

## Starter missions

V1 ships with original mission templates for:

1. **Deep Research** — evidence gathering, synthesis, citation checking, and verification.
2. **Build** — plan, implement, test, verify, summarize.
3. **Monitor** — define condition, schedule/continuous execution, memory, alert only on meaningful change.
4. **Business Ops** — research, analyze, produce an action plan or operational artifact, verify assumptions.
5. **Daily Brief** — summarize scheduled/recent inputs into decisions, risks, and next actions.

Mission templates are documentation/prompt assets, not a separate workflow runtime in V1.

## Configuration

Add a new preset named `agent-os-v1` under `configs/openjarvis/examples/` and expose it through `jarvis init --preset agent-os-v1`.

The preset should:

- use the existing `orchestrator` agent;
- enable memory context and persistent SQLite storage;
- expose a conservative but useful tool set;
- enable MCP, telemetry, and traces;
- keep the API server bound to loopback;
- use Ollama/local-first defaults suitable for a normal workstation rather than the repository's benchmark config;
- include an original Agent OS objective describing planning, delegation, verification, and memory behavior.

## Documentation package

Create `docs/agent-os-v1/` containing:

- `README.md` — quick start and operating model;
- `AGENTS.md` — role contracts;
- `MISSIONS.md` — five starter mission templates;
- `MEMORY.md` — what to remember and what not to persist.

## CLI change

Add `agent-os-v1` to the allowed values for the existing `--preset` option in `src/openjarvis/cli/init_cmd.py`. No new CLI command is required for V1.

## Testing

Add/extend CLI tests so `agent-os-v1` is accepted by Click and installs the corresponding preset into a temporary config location. Existing preset behavior must remain unchanged.

## Non-goals for V1

- Wake word or voice pipeline changes
- New desktop visual design
- Dedicated long-lived process per role
- DAG mission database
- New approval engine
- Knowledge graph
- Autonomous skill generation
- Multi-model cost governor

Those belong in later JARVIS phases after this starter Agent OS is stable.

## Acceptance criteria

V1 is complete when:

1. `jarvis init --preset agent-os-v1` is a valid CLI invocation.
2. The preset uses the existing orchestrator, persistent memory, traces, MCP, and loopback server defaults.
3. The repository contains original role, mission, and memory operating docs.
4. A user can follow the V1 README from installation to a first Agent OS objective without needing private third-party materials.
5. Tests cover the new preset path without breaking existing preset tests.
