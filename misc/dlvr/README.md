## Overview
- This is a simple cron parser written in Python.
- Source code + tests are combined in one single file cron.py

## Design
- The Cron class takes in the input, do validation and parse the output.
- Each time unit has a fixed range precomputed. The result is the intersection of this range and user input.
- The cron supports syntax for wildcard, list, range, step operators.
- Final result is kept in a dictionary and report is populated via a template.
- The cron parser can also handle redundant whitespaces.

### Usage
- python cron.py "* * * * * whoami"

### Requirements
- Python 3.x