"""

Single Category Filter
Allows you to break up the data using a categorisation column
You can either filter for a specific category, no filtering at all, or generate a dataset for each category

TODO: Allow the Filter to process the dataset to dynamically generate the categories upfront

"""

from cohorts.models.data.member import Member


def no_filter(dataset):
    return [(dataset, None)]

def _single_filter(dataset, category):
    n_dataset = []
    for member in dataset:
        filtered_entries = []
        for entry in member.entries:
            if entry.category == category:
                filtered_entries.append(entry)
        if len(filtered_entries) > 0:
            n_dataset.append(Member(filtered_entries, member.id))
    return [(n_dataset, category)]

def single_filter(category):
    return lambda dataset: _single_filter(dataset, category)

def split_dataset(dataset):
    datasets = []
    category_map = {}

    for member in dataset:
        member_category_map = {}
        for entry in member.entries:
            if entry.category in member_category_map:
                member_category_map[entry.category].append(entry)
            else:
                member_category_map[entry.category] = [entry]
        for category in member_category_map:
            if category in category_map:
                category_map[category].append(member)
            else:
                category_map[category] = [member]

    for category in category_map:
        datasets.append((category_map[category],category))

    return datasets

