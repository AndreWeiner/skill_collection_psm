# Voice input on Linux

Audio is sent to the TUD:AI transcription endpoint using `alias-stt` and
`SCADSAI_API_KEY`. Use a microphone and recordings appropriate for that service.
These tools are Linux utilities, not ChatGPT/OpenCode plugin packages.

## OpenCode fixed-duration dictation

On Debian/Ubuntu the helper needs `alsa-utils`, `curl` and `jq`:

```bash
sudo apt install alsa-utils curl jq
mkdir -p ~/.local/bin ~/.config/opencode/commands
install -m 755 tools/voice/voice-record.sh ~/.local/bin/opencode-voice-record
cp -n opencode/commands/voice.md ~/.config/opencode/commands/voice.md
```

Run from this checkout. If the command file already exists, compare/merge it
instead of overwriting. Ensure `~/.local/bin` is in PATH and the OpenCode launch
environment contains `SCADSAI_API_KEY` (see [setup](opencode-tu-dresden.md)).
Restart OpenCode, then use `/voice 5`. Test the helper independently with
`opencode-voice-record 5`; it prints the transcript and removes its temporary WAV.
Use `arecord -l` and your desktop sound settings to select/check the microphone.

## Existing desktop toggle

`tools/voice/voice-toggle.sh` preserves the author's original KDE-oriented helper.
First invocation starts recording; the second stops, transcribes and puts text
in KDE Klipper. It tries terminal paste through ydotool when available.

```bash
mkdir -p /tmp/opencode ~/.local/bin
install -m 755 tools/voice/voice-toggle.sh ~/.local/bin/voice-toggle.sh
```

Bind `~/.local/bin/voice-toggle.sh` to a shortcut in KDE System Settings.
It needs the above audio/HTTP tools plus `qdbus6` and KDE Klipper; `kdialog` is
optional for notifications. ydotool and its daemon are optional. Paste manually
when automatic paste is unavailable; terminal `Ctrl+Shift+V` is application
specific. Other desktops need a clipboard adaptation.

Ensure the shortcut launch environment receives the key. The original helper
also tries to read a simple `export SCADSAI_API_KEY=...` line from `.bashrc`;
that fallback is not a general credential loader. Its `/tmp/opencode` directory
must be recreated after a reboot. It uses fixed PID/WAV filenames, has limited
error handling, leaves the last recording on disk, and is intended for one
local user/session. Remove that recording after use. The fixed-duration helper
above is preferable when these limitations matter.

Microphone capture, transcription service access, shortcut dispatch and paste
must each be tested on the target workstation. Packaging and syntax checks do
not establish that desktop dictation works.
