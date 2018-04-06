from cohorts.models.data.member import *

def datamodel(entry_parse_fn):
    return lambda dataframe: members_parsers(dataframe, entry_parse_fn)

def members_parsers(dataframe, entry_parse_fn):
    entries = []
    for entry in dataframe:
        parsed_entry = entry_parse_fn(entry)
        entries.append(parsed_entry)
    members = {}
    for entry in entries:
        ID = entry.id
        if ID in members:
            members[ID].append(entry)
        else:
            members[ID] = [entry]
    dataset = []
    for member_id in members:
        m = Member(members[member_id], member_id)
        dataset.append(m)

    return dataset