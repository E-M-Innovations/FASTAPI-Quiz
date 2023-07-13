def serializeDict(a) -> dict:
    """
    Serialize ObjectId to str
    """
    return {
        **{i: str(a[i]) for i in a if i == "_id"},
        **{i: a[i] for i in a if i != "_id"},
    }


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
