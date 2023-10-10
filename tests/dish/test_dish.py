import pytest

from src.models.dish import Dish
from src.models.ingredient import Ingredient

# Req 2


def test_dish():
    dish = Dish("ingr", 20.0)
    assert dish.__repr__() == "Dish('ingr', R$20.00)"

    ingredient = Ingredient("presunto")
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.name == "ingr"

    dish2 = Dish("ingr2", 20.0)

    assert dish.__hash__() != dish2.__hash__()
    assert dish.__hash__() == dish.__hash__()

    assert dish.__eq__(dish2) is False
    assert dish.__eq__(dish) is True

    with pytest.raises(TypeError):
        Dish("ingr", "20.0")

    with pytest.raises(ValueError):
        Dish("ingr", -20.0)

    assert dish.get_restrictions() == ingredient.restrictions

    assert dish.get_ingredients() == {ingredient}
