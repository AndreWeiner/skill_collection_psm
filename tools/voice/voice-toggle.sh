#!/usr/bin/env bash
# Voice dictation toggle: first invocation starts recording, second invocation
# stops recording, transcribes via scads.ai and inserts the text into the
# focused window (auto-typed if ydotoold is running, clipboard otherwise).

PIDFILE="/tmp/opencode/voice-dictation.pid"
WAV="/tmp/opencode/voice-dictation.wav"
URL="https://llm.scads.ai/v1/audio/transcriptions"
MODEL="alias-stt"

notify() {
    command -v kdialog >/dev/null 2>&1 &&
        kdialog --title "Voice dictation" --passivepopup "$1" 3 >/dev/null 2>&1 &
}

key="${SCADSAI_API_KEY:-$(grep -oP '^export SCADSAI_API_KEY=\K.*' "$HOME/.bashrc" 2>/dev/null | tail -1)}"
key="${key%\"}"; key="${key#\"}"; key="${key%\'}"; key="${key#\'}"

if [[ -f "$PIDFILE" ]] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    kill -INT "$(cat "$PIDFILE")" 2>/dev/null
    rm -f "$PIDFILE"
    sleep 0.5
    text=$(curl -s -m 60 "$URL" -H "Authorization: Bearer $key" \
        -F file=@"$WAV" -F model="$MODEL" | jq -r '.text')
    text="${text# }"
    if [[ -z "$text" || "$text" == "null" || -z "${text//[[:space:].,]/}" ]]; then
        notify "Nothing transcribed"
        exit 1
    fi
    qdbus6 org.kde.klipper /klipper setClipboardContents "$text" >/dev/null 2>&1
    if command -v ydotool >/dev/null 2>&1 && [[ -r /dev/uinput ]]; then
        sleep 0.3
        ydotool key ctrl+shift+v
        notify "Transcribed and pasted: $text"
    else
        notify "Transcribed → clipboard (Ctrl+Shift+V to paste): $text"
    fi
else
    rm -f "$WAV"
    arecord -q -f S16_LE -r 16000 -c 1 "$WAV" 2>/dev/null &
    echo $! > "$PIDFILE"
    notify "Recording — press hotkey again to stop"
fi
