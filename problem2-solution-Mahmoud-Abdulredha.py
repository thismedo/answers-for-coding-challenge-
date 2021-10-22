fridge = {"banana": 1, "orange": 2, "mashroom": 3, "apple": 4}
ingredients = {"apple": 4, "banana": 1}


def validateRecipeWithQuantity():
    if ingredients in fridge:
        return True 
    else: False
