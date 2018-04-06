# cohorts
cohorts.py makes generating cohort analysis from raw data a magical experience

## Introduction to Cohort Analysis

Cohort Analysis is a analysis/reporting technique to show the evolution of lifetime-behaviour in your system over time, noting that the members of the system are dynamic and that your system is dynamic. To give an example, you might run a Pizza restaurant. Customers that buy in a certain month may or may not come back later and buy more. They eventually will die, or move away from your Pizza restaurant. But over time, you may change the way you run the Pizza restaurant. And that will change the lifetime-behaviour of your Customers too.

Cohort Analysis is important because a single metric (e.g. Average Lifetime spend per Customer) doesn't tell you how their behaviour changes over time and doesn't explain why this metric might fluctuate over time.

Cohort Analysis represents a metric in two dimensions (over time for each cohort of customers), and over different cohorts (usually based on when that cohort first ordered).

# Our Model of Cohort Analysis

In order to do Cohort Analysis, you need to define the following things:
1. Dataset : where is the base data that this comes from
2. Data Model: identifies which columns in your data are important
3. Time Model: how do you pick your cohort (e.g. based on the month of first order) and how do you evolve it over time (monthly)
4. Metric Model: what are you trying to track (e.g. % of customers that buy each month from the original cohort size)
5. Filter Model: you might want to look at the analysis for each of your restaurants, or focus on a specific restaurant
 
The cohorts.py library defines how these models combine, but give you the flexibility of defining your own models. Over time, we hope to build up a bank of models that will cover 90% of needs.

# Using the cohorts.py

The best way to start understanding it is to follow through the marketplace.py exaple in examples/three_sided_marketplace/marketplace.py

The data (marketplace_data_example.csv) contains the following columns:
timestamp: a date in format DD/MM/YYYY HH:MM
city: the city of operation e.g. Tokyo, Paris
customerID: unique ID for customers
driverID: unique ID for drivers
merchantID: unique ID for merchants
spend: a numeric field representing the customer's spend (for a single order)
Each entry is a single order

Running marketplace.py does the following things:
1. Loads the CSV file into a simple dataframe (which is just a list of keyed entries)
2. Creates a CohortTable using a Datamodel, Timemodel, Filtermodel, Metricmodel and the dataframe. These models are implemented in the main library
3. Calls generate() which executes the creation of the cohort data
4. For each Cohort Table output, it prints this (there's one for each City, which is used as a sub-category).

Prints to Console a table you can easily copy straight into Excel.

```
Paris	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	Cohort Size
2017-01-01 00:00:00	1.0	0.21359223300970873	0.2621359223300971	0.3786407766990291	0.4563106796116505	0.3300970873786408	0.24271844660194175	0.36893203883495146	0.2524271844660194	0.3786407766990291	0.4368932038834951	0.5048543689320388	0.39805825242718446	0.49514563106796117	0.5145631067961165	103
2017-02-01 00:00:00	1.0	0.2647058823529412	0.3627450980392157	0.5196078431372549	0.2647058823529412	0.28431372549019607	0.28431372549019607	0.30392156862745096	0.3235294117647059	0.4019607843137255	0.3137254901960784	0.35294117647058826	0.29411764705882354	0.3431372549019608		102
2017-03-01 00:00:00	1.0	0.2976190476190476	0.4107142857142857	0.2619047619047619	0.22023809523809523	0.20833333333333334	0.17261904761904762	0.25	0.3273809523809524	0.2916666666666667	0.30357142857142855	0.2857142857142857	0.32142857142857145			168
2017-04-01 00:00:00	1.0	0.4294478527607362	0.22085889570552147	0.18404907975460122	0.2331288343558282	0.17791411042944785	0.31901840490797545	0.26993865030674846	0.2147239263803681	0.3128834355828221	0.3374233128834356	0.31901840490797545				163
2017-05-01 00:00:00	1.0	0.2445414847161572	0.1615720524017467	0.2052401746724891	0.1965065502183406	0.2838427947598253	0.32751091703056767	0.2576419213973799	0.31004366812227074	0.34934497816593885	0.42358078602620086					229
2017-06-01 00:00:00	1.0	0.2916666666666667	0.2760416666666667	0.19270833333333334	0.2864583333333333	0.3125	0.3020833333333333	0.375	0.3697916666666667	0.375						192
2017-07-01 00:00:00	1.0	0.3443708609271523	0.32450331125827814	0.36423841059602646	0.3973509933774834	0.3509933774834437	0.4370860927152318	0.3841059602649007	0.4768211920529801							151
2017-08-01 00:00:00	1.0	0.25	0.38125	0.375	0.33125	0.46875	0.35625	0.4								160
2017-09-01 00:00:00	1.0	0.33858267716535434	0.36220472440944884	0.31496062992125984	0.41732283464566927	0.33858267716535434	0.3858267716535433									127
2017-10-01 00:00:00	1.0	0.34	0.29	0.315	0.37	0.48										200
2017-11-01 00:00:00	1.0	0.2911392405063291	0.3037974683544304	0.3227848101265823	0.33544303797468356											158
2017-12-01 00:00:00	1.0	0.37777777777777777	0.3037037037037037	0.3925925925925926												135
2018-01-01 00:00:00	1.0	0.3310344827586207	0.33793103448275863													145
2018-02-01 00:00:00	1.0	0.44														100
2018-03-01 00:00:00	1.0															104
```

# Notes on F27 Ventures
F27 was started by a group of 27-year olds who wanted to change the world one code commit at a time. We've worked at startups, large corporates and gone freelance. You don't have to be 27 to be part of our journey, you just need to dig what we do.
