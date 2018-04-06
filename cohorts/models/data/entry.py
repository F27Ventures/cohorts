class Entry:
    timestamp = None
    total = 0.0
    id = 0
    category = None

    def __init__(self, timestamp, total, id, category):
        self.timestamp = timestamp
        self.total = total
        self.id = id
        self.category = category
