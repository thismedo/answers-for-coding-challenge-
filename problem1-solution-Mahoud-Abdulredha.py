fridge = [potatoe, tomatoe, mushroom, broccoli]
ingredients = [mushroom, potatoe]


def validateRecipe():
    if ingredients in fridge:
        return True 
    else:
        False


