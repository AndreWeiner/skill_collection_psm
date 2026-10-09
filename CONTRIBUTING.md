# Contributing

People and agents use the same workflow: fork, create a focused branch, make
and verify changes, then open a pull request against this repository's `main`.
For substantial new workflows or behavior changes, describe the intended scope
in an issue first so maintainers can give feedback. Small fixes can go directly
to a pull request. Maintainers review and merge contributions.

## 1. Fork and clone

Open [the repository](https://github.com/AndreWeiner/skill_collection_psm) and
click **Fork** to create a copy under your own GitHub account. Replace
`YOUR-USERNAME` below with that account name:

```bash
git clone https://github.com/YOUR-USERNAME/skill_collection_psm.git
cd skill_collection_psm
git remote add upstream https://github.com/AndreWeiner/skill_collection_psm.git
git remote -v
```

`origin` is your fork; `upstream` is the maintained collection. HTTPS pushes
require GitHub authentication, such as GitHub CLI's credential integration or
a token; your GitHub password does not authenticate Git pushes.

## 2. Create a branch from current upstream

Start with a clean working tree. Fetch upstream and create a new branch for
one coherent change (replace `docs/improve-setup` with a descriptive name):

```bash
git status --short
git fetch upstream
git switch -c docs/improve-setup upstream/main
```

Do not mix unrelated changes or generated experiment outputs into the branch.
Read [AGENTS.md](AGENTS.md), the affected skill, and its relevant references.

## 3. Make and verify the change

- Keep skill sources in `skills/<name>/`, with matching frontmatter `name` and
  a concise description. Include the complete references/scripts/assets needed.
- Update [the catalog](docs/catalog.md) for new skills or changed dependencies,
  compatibility and invocation examples. Avoid colliding with bundled skills.
- Keep OpenCode extensions under `opencode/`, desktop helpers under `tools/`,
  and installation helpers under `scripts/`. Update the corresponding guide.
- Use credential placeholders/environment references. Exclude keys, recordings,
  private inputs, dependency trees and local validation output from commits.
- Verify actual behavior when helpers change. Do not make remote model calls,
  record audio or change global host configuration merely to test documentation.

For helper/style changes, run the relevant existing tests. For the full suite,
use a Python environment containing Matplotlib and Pillow:

```bash
python3 -m unittest discover -s tests -v
```

The scientific style's LaTeX export check also needs `latex` and `dvipng`; it
skips if they are absent. For a focused change, a test module can be run directly,
for example `python3 -m unittest discover -s tests -p test_image_review.py -v`.
Report missing dependencies, skips and untested host/service behavior accurately.

For documentation changes, check local links, paths and commands, and review
consistency using [report-consistency](skills/report-consistency/SKILL.md).
For discovery changes, check the skill list in the target host and state its
version. Documentation-only changes do not require unrelated API or audio tests.

Before committing, inspect the diff and stage only intended files:

```bash
git diff --check
git diff
git add CONTRIBUTING.md
git diff --cached
git commit -m "Clarify contribution workflow"
```

The filename and commit message above are examples; use the files and message
appropriate to your change. Inspect `git status` for untracked files as well.

## 4. Push and open a pull request

```bash
git push -u origin HEAD
```

On GitHub, open your fork and choose **Compare & pull request**, or open a new
pull request in the upstream repository and select **compare across forks**.
Check the base repository is `AndreWeiner/skill_collection_psm`, base branch is
`main`, and the head repository/branch are your fork and feature branch.
Use a draft pull request if work or validation is still incomplete.

The [pull request template](.github/pull_request_template.md) asks for the
problem, resulting behavior, relevant checks and remaining limitations. Include
host/version information for integration changes. Never paste credentials or
private service responses into the pull request.

With GitHub CLI, an authenticated contributor can instead run:

```bash
gh pr create --repo AndreWeiner/skill_collection_psm --base main --head YOUR-USERNAME:docs/improve-setup
```

Replace the username/branch and follow the interactive title/body prompts.
See [GitHub's fork pull request guide](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork).

## 5. Respond to review and stay current

Make requested fixes on the same feature branch, commit, and push to `origin`;
the existing pull request updates automatically. If upstream changes require
synchronization, start from a clean working tree on your feature branch:

```bash
git fetch upstream
git merge upstream/main
```

Resolve any conflicts, recheck the affected behavior, commit the resolution if
needed, and push again. Prefer this merge workflow over rewriting a branch
already being reviewed. After the pull request is merged, create future feature
branches from freshly fetched `upstream/main` as above.

## Agent contributions

Agents should follow this guide and repository instructions, inspect remotes
before pushing, and preserve unrelated user changes. Use the contributor's fork
and a feature branch; do not push directly to upstream `main`. Prepare a concrete
patch and validation evidence within the authorized task. Creating a fork,
pushing commits, opening a pull request or merging still depends on the user's
authorization and host permissions; this guide itself does not grant them.
Record what actually ran and any remaining limitations in the pull request.

## Licensing

No redistribution license has been selected. Public visibility and GitHub's
forking features do not by themselves supply a general reuse license. Contact
the maintainer about reuse or contribution licensing terms before submitting
material whose permissions are unclear.
