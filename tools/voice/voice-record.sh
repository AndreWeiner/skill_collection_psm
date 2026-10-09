#!/usr/bin/env bash
# Capture a bounded recording; print its TUD:AI transcript.
set -euo pipefail
seconds="${1:-5}"
if [[ $# -gt 1 || ! "$seconds" =~ ^[0-9]+$ || ${#seconds} -gt 3 ]]; then
    echo 'Usage: opencode-voice-record [seconds: 1-120]' >&2
    exit 2
fi
seconds=$((10#$seconds))
if (( seconds < 1 || seconds > 120 )); then
    echo 'Recording duration must be between 1 and 120 seconds' >&2
    exit 2
fi
: "${SCADSAI_API_KEY:?Set SCADSAI_API_KEY in the launch environment}"
for dependency in arecord curl jq; do
    command -v "$dependency" >/dev/null || { echo "Missing dependency: $dependency" >&2; exit 1; }
done
recording_dir=$(mktemp -d)
trap 'rm -rf -- "$recording_dir"' EXIT
arecord -q -d "$seconds" -f S16_LE -r 16000 -c 1 "$recording_dir/voice.wav"
curl --fail --silent --show-error --max-time 60 \
    https://llm.scads.ai/v1/audio/transcriptions \
    -H "Authorization: Bearer $SCADSAI_API_KEY" \
    -F "file=@$recording_dir/voice.wav" -F model=alias-stt |
    jq -er '.text | select(type == "string" and test("\\S"))'
