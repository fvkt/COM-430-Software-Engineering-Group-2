"""
Pet Rock Genie Test Stage Runner
Simulates a scripted session to exercise Test Stage behavior
and captures a log snapshot for verification.
"""
import subprocess
import sys
import json
from pathlib import Path

def run_session(input_lines, env=None):
    # Run the Pet Rock Genie in a subprocess
    # Assumes main entrypoint is main.py or pet_rock_genie.py
    # Adjust the command if your entrypoint differs
    cmd = [sys.executable, "pet_rock_genie.py"]
    if not Path(cmd[1]).exists():
        # fallback to main.py
        cmd = [sys.executable, "main.py"]

    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=env
    )

    # Feed inputs
    out, _ = proc.communicate(input="\n".join(input_lines) + "\n")
    return_code = proc.returncode
    return out, return_code

def main():
    # Prepare a small scripted session
    inputs = [
        "Will this rock pass the test?",   # normal question
        "",                                 # empty input
        "Is Python awesome?",               # no question mark
        "quit"                              # exit
    ]
    # Run with default environment; you can override ENV vars if desired
    output, code = run_session(inputs)
    # Save a log snapshot if pet_rock_genie_v2.log is created
    log_path = Path("pet_rock_genie_v2.log")
    snapshot = {
        "exit_code": code,
        "log_exists": log_path.exists(),
        "log_path": str(log_path.resolve()) if log_path.exists() else None,
        "output": output
    }
    with open("test_snapshot.json", "w") as f:
        json.dump(snapshot, f, indent=2)

    print("Test snapshot written to test_snapshot.json")

if __name__ == "__main__":
    main()
