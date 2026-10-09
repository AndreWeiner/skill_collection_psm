# OpenCode at TU Dresden

## Access and installation

TUD:AI is provided by ScaDS.AI and ZIH. TU Dresden employees can generate a
personal API key through the [self-service portal](https://selfservice.tu-dresden.de/services/scads-llm-api/).
Students and members of affiliated institutes can request access from
llm.scads.ai@tu-dresden.de. See the [official access instructions](https://llm.scads.ai/docs/usage/api/).

Install the OpenCode CLI using an option from the
[official installation guide](https://opencode.ai/docs/), for example with an
existing Node.js/npm installation:

```bash
npm install -g opencode-ai
opencode --version
```

The local source setup used OpenCode 1.18.35 when this guide was prepared on
2026-10-09. Check your version's schema before adapting configuration.
The desktop application is available from the
[official download page](https://opencode.ai/download).

## Configure the provider

From this checkout, create the configuration directory:

```bash
mkdir -p ~/.config/opencode
```

For a fresh installation, copy `opencode/opencode.example.json` to
`~/.config/opencode/opencode.json`. If that file already exists, merge its
`provider.scads` entry and choose the default `model` deliberately; do not
replace unrelated settings. The example reads the key from the environment.

Set it for the current terminal without putting it in shell history:

```bash
read -rsp 'TUD:AI API key: ' SCADSAI_API_KEY; echo
export SCADSAI_API_KEY
```

For persistence, use your institution-approved credential storage or a private
shell startup file. A desktop launcher does not necessarily inherit terminal
variables; launch `opencode` from this terminal for the first check. Never share
or commit the key. The service's usage policy governs data and credentials.

The provider uses `@ai-sdk/openai-compatible` and
`https://llm.scads.ai/v1`. `scads` is this collection's local provider identifier.
The example selects `scads/alias-code`; aliases can change their backing model.
For reproducible comparisons, record the model actually reported by the service.

## Verify and launch

```bash
opencode models scads
opencode
```

Use `/models` to inspect/select the configured model and submit a small task in
a disposable project. A catalog entry alone does not prove successful inference.
If authentication fails, check that the launch environment contains the key
without printing it. For rate limits or server errors, follow the service's
response rather than repeatedly retrying. Current model availability is in the
[TUD:AI model catalog](https://llm.scads.ai/docs/models/).

Then follow [skill installation](installation.md) and optionally
[extensions](opencode-extensions.md). No GWDG account or provider is required
for this ScaDS-only example.
