"""

This example shows how to generate a raft of Cohort Data reporting for a 3-sided marketplace.
In this example, there are Customers, Drivers and Merchants.
The data is needed for Monthly Cohorts.

The data is also annotated with City (that's the categorisation).
Each entry is an order with an associated Customer, Driver, Merchant, City and Spend (as a float).

"""

from cohorts.generator import CohortTable, load_data
from cohorts.models.timestep.standard import TimeModelMonthly
from cohorts.models.filters.single_category import no_filter, split_dataset
from cohorts.models.metrics.basic import *
from cohorts.models.data.entry import *
from cohorts.models.data.simple_pass import *
from datetime import datetime

data_file = "marketplace_data_example.csv" # Filepath for CSV data

dataframe = load_data(data_file)

def user_parse_fn(entry):
    TS = datetime.strptime(entry['timestamp'], "%d/%m/%Y %H:%M")
    category = entry['city']
    ID = entry['customerID']
    total = entry['spend']
    return Entry(TS, total, ID, category)

def driver_parse_fn(entry):
    TS = datetime.strptime(entry['timestamp'], "%d/%m/%Y %H:%M")
    category = entry['city']
    ID = entry['driverID']
    total = entry['spend']
    return Entry(TS, total, ID, category)

def merchant_parse_fn(entry):
    TS = datetime.strptime(entry['timestamp'], "%d/%m/%Y %H:%M")
    category = entry['city']
    ID = entry['merchantID']
    total = entry['spend']
    return Entry(TS, total, ID, category)

CT = CohortTable(datamodel=datamodel(user_parse_fn), timemodel=TimeModelMonthly,
                 filtermodel=split_dataset, metricmodel=MetricPercentActive,
                 data_frame=dataframe)

results = CT.generate()

for r in results:
    print(r[0])

