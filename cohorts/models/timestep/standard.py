"""

Provides the standard timestep use cases most people will need

Daily
Weekly
* Monthly - most common for investors
Yearly

A timemodel consists simply of two functions
1. Identify Cohort - Usually this is based on their first order
2. Identify Timestep for an entry

TODO: Add Quarterly Timestep

"""

import datetime

class TimeModel:

    identify_cohort = None
    identify_timestep = None

    def __init__(self, cohort_fn, timestep_fn):
        self.identify_cohort = cohort_fn
        self.identify_timestep = timestep_fn

def first_order_yearly(member):
    # Assumes member consists of entries each with a timestamp
    earliest_date = datetime.datetime(9999, 1, 1)

    # Find earliest date in records for this member
    for entry in member.entries:
        dt = entry.timestamp
        if dt < earliest_date:
            earliest_date = dt

    FOY = datetime.datetime(earliest_date.year, 1, 1)

    return FOY


def first_order_month(member):
    # Assumes member consists of entries each with a timestamp
    earliest_date = datetime.datetime(9999, 1, 1)

    # Find earliest date in records for this member
    for entry in member.entries:
        dt = entry.timestamp
        if dt < earliest_date:
            earliest_date = dt

    FOM = datetime.datetime(earliest_date.year, earliest_date.month, 1)

    return FOM

def first_order_week(member):
    earliest_date = datetime.datetime(3999,1,1)

    for entry in member.entries:
        dt = entry.timestamp
        if dt < earliest_date:
            earliest_date = dt

    FOW = earliest_date + datetime.timedelta(0-earliest_date.weekday())
    FOW = datetime.datetime(FOW.year, FOW.month, FOW.day)

    return FOW

def first_order_day(member):
    # Assumes member consists of entries each with a timestamp
    earliest_date = datetime.datetime(9999, 1, 1)

    # Find earliest date in records for this member
    for entry in member.entries:
        dt = entry.timestamp
        if dt < earliest_date:
            earliest_date = dt

    FOD = datetime.datetime(earliest_date.year, earliest_date.month, earliest_date.day)

    return FOD

def granularity_yearly(FOM, TS):
    return (TS.year - FOM.year)

def granularity_monthly(FOM, TS):
    return (TS.year - FOM.year) * 12 + (TS.month - FOM.month)

def granularity_weekly(FOW, TS):
    return (TS - FOW).days // 7

def granularity_daily(FOD, TS):
    return (TS - FOD).days

TimeModelYearly = TimeModel(first_order_yearly, granularity_yearly)
TimeModelMonthly = TimeModel(first_order_month, granularity_monthly)
TimeModelWeekly = TimeModel(first_order_week, granularity_weekly)
TimeModelDaily = TimeModel(first_order_day, granularity_daily)





