

def validate_ingredients(ingredients: str) -> str:
    if ingredients is "fire" or ingredients is "water":
        return f"{ingredients} - VALID"
    elif ingredients is "earth" or ingredients is "air":
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"