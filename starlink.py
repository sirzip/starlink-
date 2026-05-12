#!/usr/bin/env python3
import starlink
import sys

# Force flush output
sys.stdout.flush()
sys.stderr.flush()

# Run with print wrapper
try:
    result = starlink.run_extreme()
    print("Scanner finished")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.stderr.flush()