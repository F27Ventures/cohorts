""" Generator of Cohort Tables

A Cohort Table is made up of:
- Data File or a Data Frame
- Data Model to interpret columns
- Time Model to decide how to separate the cohorts and look at their progression over tiem
- Filter Model to sub-categorise or filter out entries e.g. split by city, or only look at a particular city
- Metric Model to decide what metric we are measuring for each cohort over time

Often, you will generate many different Cohort Tables from one Data File.
In this case, it is better to first load the data into a data frame and then re-use this.

The output of the Cohort Table function is one (or more tables through sub-categorisation) which can be exported to CSV
and easily imported into Excel/Powerpoint or other for presentation purposes

"""

import csv
import logging
import sys
from typing import Dict


class CohortTable:

    data = None  # Data Frame
    model_data = None
    model_time = None
    model_filter = None
    model_metric = None

    def __init__(self, datamodel, timemodel, filtermodel, metricmodel, data_file: str = None, data_frame=None):
        self.model_data = datamodel
        self.model_time = timemodel
        self.model_filter = filtermodel
        self.model_metric = metricmodel

        if data_file is not None:
            self.data = load_data(data_file)
        elif data_frame is not None:
            self.data = data_frame
        else:
            # Raise Error about data
            raise Exception("Error with Data File or Data Frame")



    def generate(self):

        results = []

        # Step 1. Apply the Data Model to the Data Frame
        processed_data = self.model_data(self.data)

        # Step 2. Loop through and Apply Filters
        filtered_datasets = self.model_filter(processed_data)
        for dataset, category in filtered_datasets:

            # Step 3. Generate Single Cohort Table
            cohort_matrix, cohort_sizes = generate_cohorts(dataset,
                                                           self.model_time,
                                                           self.model_metric)

            # Step 4. Convert this into an easy to use Table
            table = tabulation(cohort_matrix, cohort_sizes, category)
            results.append((table, cohort_matrix, cohort_sizes))

        return results

def load_data(data_file: str):

    data = []
    row_count = 0
    with open(data_file, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        try:
            for row in reader:
                row_count += 1
                data.append(row)
        except csv.Error as e:
            sys.exit('file {}, line{}: {}'.format(data_file, reader.line_num, e))
    logging.info("Loaded {} Rows".format(row_count))
    return data

def generate_cohorts(dataset, timemodel, metricmodel):
    cohort_matrix = {}  # Cohort x Timestep => Metric
    cohort_sizes = {}

    # Step 1. Run Single Function over the data to get the initial per member calculation
    for member in dataset:
        cohort_id = timemodel.identify_cohort(member)
        if cohort_id in cohort_sizes:
            cohort_sizes[cohort_id] += 1
        else:
            cohort_sizes[cohort_id] = 1

        for entry in member.entries:
            timestep = timemodel.identify_timestep(cohort_id, entry.timestamp)

            data = None
            if cohort_id in cohort_matrix:
                if timestep in cohort_matrix[cohort_id]:
                    data = cohort_matrix[cohort_id][timestep]
                cohort_matrix[cohort_id][timestep] = metricmodel.single_step_fn(data, entry)
            else:
                cohort_matrix[cohort_id] = {timestep: metricmodel.single_step_fn(None, entry)}

    # Step 2. Run Aggregation over the Single Metrics to produce result
    cohort_matrix_finale = {}

    for cohort_id in cohort_matrix:
        base_result = metricmodel.aggregation_fn(None, cohort_matrix[cohort_id][0])
        cohort_matrix_finale[cohort_id] = {}
        for timestep in cohort_matrix[cohort_id]:
            result = metricmodel.aggregation_fn(base_result, cohort_matrix[cohort_id][timestep])
            cohort_matrix_finale[cohort_id][timestep] = result

    return cohort_matrix_finale, cohort_sizes


def tabulation(cohort_matrix, cohort_sizes: Dict[str, int], category=None):
    # Columns are for each timestep
    # Rows are for each cohort

    # Manual but OK generally as cohorts will be small
    max_timestep = 0

    for cohort_id in cohort_matrix:
        for timestep in cohort_matrix[cohort_id]:
            if timestep > max_timestep:
                max_timestep = timestep

    s = category if category is not None else ""
    for i in range(0, max_timestep+1):
        s += "\t{}".format(i)
    s += "\tCohort Size"
    for cohort_id in sorted(cohort_matrix.keys()):
        s += "\n{}".format(cohort_id)
        for i in range(0, max_timestep+1):
            if i in cohort_matrix[cohort_id]:
                s += "\t{}".format(cohort_matrix[cohort_id][i])
            else:
                s += "\t"
        s += "\t{}".format(cohort_sizes[cohort_id])
    return s
