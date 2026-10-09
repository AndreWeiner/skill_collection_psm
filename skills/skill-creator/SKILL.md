---
name: skill-creator
description: Create or improve reusable agent skills and SKILL.md files. Use when the user asks to create a skill, turn an established workflow into a skill, or improve an existing skill's instructions, discovery, or supporting resources.
---

# Skill Creator

Produce a skill another agent can discover and use to complete the intended
task. Adapt the work to the target agent and the user's chosen scope.

## Establish the contract

Identify the requests that should activate the skill, the required inputs,
the expected output, and how successful completion can be checked. Use the
conversation and existing project conventions first. Ask only for missing
information that changes the implementation.

Inspect nearby skills and applicable project instructions before choosing a
location or adding a new definition. Improve an existing skill when it already
serves the requested purpose. Keep one-off details as parameters or examples
rather than turning them into rules for every future task.

## Write the definition

Create a folder whose name matches the skill's lowercase, hyphen-separated
name. Keep the name at most 64 characters. The entry point is `SKILL.md` with
YAML frontmatter containing nonempty `name` and `description` strings.

The description must explain the capability and when to select it. Include
the terms a user would naturally use. Add exclusions only to prevent plausible
confusion with neighboring skills. Keep it under 1024 characters for portability.

Write the body as actionable instructions for the agent. State the useful
decision rules, required inputs, output requirements, and relevant validation.
Explain fragile ordering or constraints when they affect correctness. Avoid
generic advice the agent already knows and unnecessary fixed sequences.

Keep the entry point focused. Add files only when they have a concrete use:

- `scripts/`: repeated operations that benefit from executable, deterministic code.
- `references/`: detailed guidance needed only for a particular task or mode.
- `assets/`: templates and other files used in the generated output.

Link supporting files from the entry point and explain when to read or use them.
Resolve relative paths from the skill folder. Do not make the workflow depend
on another skill, subagent, API, or tool unless it exists in the target setup;
describe a practical fallback when appropriate.

## Preserve scope and portability

Honor explicit user choices and existing authorization. Creating a skill does
not authorize publishing, sending messages, changing unrelated settings, or
running its future external actions during validation.

Use environment variables or configuration for credentials; never embed secrets.
Document required dependencies without assuming they are installed. Add
provider-specific metadata only when the intended host needs it. Preserve
existing invocation settings when updating a skill.

For an existing definition, inspect its supporting files and callers before
removing them. Make the smallest change that addresses the requested behavior.

## Check the result

Check frontmatter types, naming, linked file paths, unfinished placeholders,
and consistency between the description and the actual workflow. Run new or
changed helper scripts on suitable local fixtures.

Review realistic requests: one that should activate the skill, a related one
that should not, and a case with incomplete inputs. A review of these prompts
is a design check, not an execution test. To test behavior, actually apply the
skill to a representative request in an isolated workspace and inspect the
output against the task's acceptance criteria. For consequential
or complex workflows, perform an isolated behavioral trial when the required
tools and authorization are available. Do not claim a trial was run when only
the instructions were reviewed.

Fix demonstrated problems, then report the resulting file location, intended
use, validation performed, and any remaining dependency or discovery limitation.

## Register for the chosen host

Use the location requested by the user. Otherwise follow the host's supported
discovery paths and the project's conventions. Read
[host integration](references/host-integration.md) when installing or making
the same skill available in more than one agent.

Check for a name collision in the target host before registration. Do not
silently shadow a built-in or existing skill: update the intended existing
definition or choose a distinct name and update its folder and frontmatter.

After registration, check discovery using the host's available inventory tools
when practical. Distinguish a saved skill from one actually discovered by the
host. Existing sessions may need to be restarted to load new skills.

## Public implementations

For an upstream implementation or a more extensive evaluation workflow, consult
the official [OpenAI skill-creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)
or [Anthropic skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator).
Inspect their current files and licenses before copying or redistributing them.
This skill is a locally authored portable workflow, not an official vendor skill.
