def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "userName": user["userName"],
        "password": user["password"]
    }

def usersEntity(entity) -> list:
    return [userEntity(user) for user in entity]