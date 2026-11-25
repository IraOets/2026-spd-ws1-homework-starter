
#!/usr/bin/env python3

# owner: @IraOets
# why: Prevent AI agents from force-pushing Git history.
# review-by: 2027-01-20

import json
import re
import sys


def main():
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        print("BLOCKED: Invalid hook input", file=sys.stderr)
        return 2

    if payload.get("tool_name") != "Bash":
        return 0

    command = payload.get("tool_input", {}).get("command", "")

    if not isinstance(command, str):
        print("BLOCKED: Invalid command", file=sys.stderr)
        return 2

    if re.search(r"\bgit\s+push\b[^\n]*\s(?:--force|-f)\b", command):
        print(
            "BLOCKED: Force push is prohibited by team policy.",
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
