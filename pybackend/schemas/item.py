def itemEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "typeOfItem": item["typeOfItem"],
        "fileInfpos": item["fileInfpos"]
    }

def itemsEntity(entity) -> list:
    return [itemEntity(item) for item in entity]