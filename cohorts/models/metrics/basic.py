"""

Basic Metrics should handle most of the metrics needed for Cohort Analysis

Metrics are made up of a single step function and an aggregation function

For example, suppose you want to know what percentage of your customers are still active

The single step function just counts the unique customers from the relevant entries
The aggregation function then divides this by the initial cohort size to get a percentage

As another example, suppose you want to know the Avg Spend per Active Customer each month

The Single Step calculates the total spend of customers fro the relevant entries in that month
The aggregation function then divides this by the size of the active cohort in that month

By doing it as two steps, you can handle most metrics.

"""

class Metric():

    single_step_fn = None
    aggregation_fn = None

    def __init__(self, single, aggregation):
        self.single_step_fn = single
        self.aggregation_fn = aggregation

# Q: What Percentage of Users are Active from the Original Cohort over Time
def count_active(data: set, entry):
    # data is either None or it is a set of active members (to avoid duplicate counting)
    if data is None:
        return {entry.id}
    else:
        data.add(entry.id)
        return data

def active_percentage_aggregation(base_result, data):
    if base_result is None:
        return len(data)
    else:
        if data is None:
            return 0
        else:
            return len(data) / base_result

MetricPercentActive = Metric(count_active, active_percentage_aggregation)

# Q: What is the AOV for each Cohort over Time
def AOV(data, entry):
    # data is either None or it is a tuple of (total spend, total orders)
    if data is None:
        return (entry.total, 1)
    else:
        return(data[0]+entry.total, data[1]+1)

def AOV_aggregation(_, data):
    return data[0]/data[1]

MetricAOV = Metric(AOV, AOV_aggregation)

# Q: What is the Average Orders per Customer from the Original Cohort over Time
def orders_aggregation_a(zero_result, data):
    if zero_result is None:
        return len(data[1])
    else:
        return data[0] / zero_result

def orders(data, entry):
    if data is None:
        return (1, {entry.id})
    else:
        data[1].add(entry.id)
        return (data[0]+1, data[1])


MetricOrdersPerOriginalCohort = Metric(orders, orders_aggregation_a)

# Q: What is the Average Orders per Active Customer in that Timestep over Time
def orders_aggregation_b(_, data):
    return data[0] / len(data[1])

MetricOrdersPerActiveCustomer = Metric(orders, orders_aggregation_b)

# Q: What is the Percent of Retained Spend (stored in .total) from the Original Cohort over Time
def GMV(data, entry):
    if data is None:
        return entry.total
    else:
        return data + entry.total

def GMV_aggregation(zero_result, data):
    if zero_result is None:
        return data
    else:
        if data is None:
            return 0
        else:
            return data / zero_result

MetricSpendRetention = Metric(GMV, GMV_aggregation)

