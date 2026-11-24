#!/usr/bin/env python3
"""Write one funny toaster error message to entry.txt.

The message is a single line of 1-120 characters with no trailing
newline, as the make.fun gate for this bounty requires.
"""

import os

MESSAGE = "ERROR: YOUR BAGEL HAS UNIONIZED AND REFUSES TO BE BROWNED."
MAX_CHARS = 120


def output_dir():
    """Resolve where entry.txt goes."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "output")


def validate(message):
    """Check the message against the gate: 1-120 chars, one line."""
    if not message or not message.strip():
        raise ValueError("error message must not be empty")
    if len(message) > MAX_CHARS:
        raise ValueError(
            "error message is %d chars, over the %d limit"
            % (len(message), MAX_CHARS)
        )
    if "\n" in message or "\r" in message:
        raise ValueError("error message must be a single line")
    if message != message.strip():
        raise ValueError("error message must not start or end with whitespace")
    return message


def main():
    message = validate(MESSAGE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(message)
    print("wrote %d chars to %s" % (len(message), path))


if __name__ == "__main__":
    main()
