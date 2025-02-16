# Unclosed File Handling in Python

This repository demonstrates a common error in Python: failing to close files after use.  The `unclosed_file.py` script shows the problematic code, while `closed_file.py` provides the corrected version using `with open(...)`. Unclosed files can lead to resource exhaustion and potential data loss in long-running applications or when handling numerous files.

## Problem

The `unclosed_file.py` script opens a file but does not close it, potentially causing problems.

## Solution

The `closed_file.py` script uses a `with` statement. This ensures that the file is always closed correctly, even if exceptions occur.