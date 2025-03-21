class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available_supplies = set(supplies)
        needs = {recipe : set(ingredient) for recipe, ingredient in zip(recipes, ingredients)}

        updated = True
        while updated:
            updated = False
            for recipe in recipes:
                if recipe in available_supplies:
                    continue

                if needs[recipe].issubset(available_supplies):
                    available_supplies.add(recipe)
                    updated = True

        return [recipe for recipe in recipes if recipe in available_supplies]            


# ! Explanation:
# * This function finds all possible recipes that can be made from the given supplies.
# * 1. Initialize the available_supplies set with the supplies.
# * 2. Create a dictionary called needs with recipes as keys and ingredients as values.
# * 3. Initialize a boolean variable called updated to True.
# * 4. While updated is True:
#     * Set updated to False.
#     * Iterate through the recipes.
#         * If the recipe is already in the available_supplies set, continue to the next recipe.
#         * If the ingredients of the recipe are a subset of the available_supplies:
#             * Add the recipe to the available_supplies set.
#             * Set updated to True.
# * 5. Return the recipes that are in the available_supplies set.

# ? Time Complexity:
# * The time complexity of this approach is O(n * m), where n is the number of recipes and m is the number of ingredients in each recipe.
# * This is because we iterate through the recipes and check if the ingredients of each recipe are a subset of the available supplies.

# ? Space Complexity:
# * The space complexity of this approach is O(n), where n is the number of recipes.
# * This is because we use the available_supplies set to store the recipes that can be made from the given supplies.