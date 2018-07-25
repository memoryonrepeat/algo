"""
The phone matchup coding test.

A phone company keeps record of all calls that have been successfully
established (see log_data below). For these calls, the company registers
whether they fail mid-call or complete successfully. We are interested in
computing the "success ratio", which is defined by the number of successful
calls vs. absolute number of calls that involved a party.

The format is:
date: day.month.year 24hours:minutes
caller: phone number
callee: phone number
status: COMPLETED/FAILED

When 111 would call 222 and the call would end successfully, the following
entry would show up in the log_data:
1.1.2014 12:33,111,222,COMPLETED
This call is counted as completed for both parties!
If the same call fails mid-call, the line would look like this
1.1.2014 12:33,111,222,FAILED
This call is counted as failed for both parties!

The following template shows some log data and the expected results.

Feel free to use any available modules from the standard python library.
Feel free to add more test cases as you see fit.
After you are done with this problem, please save the contents of this file
and share it with us. Also, send along an estimate of the time it took you
to complete this test.

We evaluate the submission based on: correctness, structure, appropriate
use of data structures, efficiency, appropriate use of the standard library.
"""

import datetime as dt
from collections import defaultdict

original_log_data = """1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
1.1.2014 13:01,111-222-333,111-333,FAILED
1.1.2014 13:04,111-222-333,454-333-222,FAILED
1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
2.1.2014 13:01,111-333,111-222-333,FAILED"""

# Test with duplicate rows
log_data_duplicate = """1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
1.1.2014 13:01,111-222-333,111-333,FAILED
1.1.2014 13:04,111-222-333,454-333-222,FAILED
1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
2.1.2014 13:01,111-333,111-222-333,FAILED
2.1.2014 13:01,111-333,111-222-333,FAILED
02.1.2014 13:01,111-333,111-222-333,FAILED
2.01.2014 13:01,111-333,111-222-333,FAILED
02.01.2014 13:1,111-333,111-222-333,FAILED"""

# Test with invalid rows
log_data_invalid = """1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
1.1.2014 13:01,111-222-333,111-333,FAILED
1.1.2014 13:04,111-222-333,454-333-222,FAILED
1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
2.1.2014 13:01,111-333,111-222-333,FAILED
2.1.2014 13:01,111-333,111-222-333,FAILED,FOO,BAR
2.1.2014 13:01,111-333,111-222-333,INVALID STATUS
30.2.2014 13:01,111-333,111-222-333,FAILED
29.2.2014 13:01,111-333,111-222-333,FAILED"""

# Test with conflict rows
log_data_conflict = """1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
1.1.2014 12:01,111-222-333,454-333-222,FAILED
1.1.2014 13:01,111-222-333,111-333,FAILED
1.1.2014 13:01,111-222-333,111-333,COMPLETED
1.1.2014 13:04,111-222-333,454-333-222,FAILED
1.1.2014 13:04,111-222-333,454-333-222,COMPLETED
1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
1.1.2014 13:05,111-222-333,454-333-222,FAILED
2.1.2014 13:01,111-333,111-222-333,FAILED
2.1.2014 13:01,111-333,111-222-333,COMPLETED"""

expected_result = {
    "111-222-333": "40.00%",
    "454-333-222": "66.67%",
    "111-333": "0.00%"
}

# Parse and validate each row


def parse_call(log):

    try:
        date, caller, callee, status = log.split(",")
    except ValueError:
        print("Call format is not valid. This row will be ignored.", log)
        return False

    if status != "COMPLETED" and status != "FAILED":
        print("Status is not valid. This row will be ignored.", log)
        return False

    try:
        # Validate and standardize all the dates to use zero-padded string to avoid duplicates due to different format
        date = dt.datetime.strptime(
            date, "%d.%m.%Y %H:%M").strftime("%d.%m.%Y %H:%M")
    except ValueError:
        print("Date is in wrong format or not valid. This row will be ignored.", log)
        return False

    return date, caller, callee, status


def compute_success_ratio(logdata):
    # Parse and filter out invalid rows
    logs = list(filter(lambda e: e != False, list(
        map(parse_call, logdata.split("\n")))))
    calls = {}
    # Use default nested dict to initiate count to 0
    stats = defaultdict(lambda: defaultdict(int))
    for date, caller, callee, status in logs:
        # Use hash to ignore rows with identical (date, caller, callee) and conflict status - only accept first result
        if not (date, caller, callee) in calls:
            calls[(date, caller, callee)] = status
            stats[caller]["total"] += 1
            stats[callee]["total"] += 1
            stats[caller]["completed"] = stats[caller]["completed"] + \
                1 if status == "COMPLETED" else stats[caller]["completed"]
            stats[callee]["completed"] = stats[callee]["completed"] + \
                1 if status == "COMPLETED" else stats[callee]["completed"]
    for key in stats:
        stats[key] = "{0:.2%}".format(
            stats[key]["completed"] / stats[key]["total"])
    return stats


if __name__ == "__main__":
    # All development and testing done on Python 3.6.1
    assert(compute_success_ratio(original_log_data) == expected_result)
    assert(compute_success_ratio(log_data_duplicate) == expected_result)
    assert(compute_success_ratio(log_data_conflict) == expected_result)
    assert(compute_success_ratio(log_data_invalid) == expected_result)


# gives expected python version - good
# additional test cases - very nice
# would have been better to use the csv package to parse the file
# good error handling
# good variable names
# dates are parsed and checked which is good - but this is not required
# 'e!=False' could be written as just 'not e' (parse_call could also return None to indicate filtered rows)
# log lines are read twice (in parse_call and 'for .. in logs') - this could have been done in a single loop
# some duplication for caller and callee code in stats
# avoids counting duplicate rows - this is nice although the stored status is never used/checked, could have used a set
