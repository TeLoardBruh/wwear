def itemEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "typeOfItem": item["typeOfItem"],
        "fileInfpos": item["fileInfpos"],
        "userId": str(item["userId"])
    }

def itemsEntity(entity) -> list:
    return [itemEntity(item) for item in entity]