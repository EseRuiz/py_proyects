class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    if ordered_id != list(range(len(ordered_id))):
        raise ValueError("Record id is invalid or out of order.")
    trees = []
    for i, j in enumerate(records):
        if j.record_id < j.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        if j.record_id == j.parent_id and j.parent_id != 0:
            raise ValueError("Only root should have equal record and parent id.")
        trees.append(Node(i))
    for i, record in enumerate(records):
        if trees[i].node_id != 0:
            trees[record.parent_id].children.append(trees[i])
    return trees[0] if trees else None