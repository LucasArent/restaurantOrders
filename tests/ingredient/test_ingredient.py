from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("queijo parmesão")
    ingredient_2 = Ingredient("presunto")
    ingredient_3 = Ingredient("presunto")

    assert ingredient_1.__hash__() != ingredient_2.__hash__()
    assert ingredient_1.__hash__() == ingredient_1.__hash__()
    assert ingredient_1.__eq__(ingredient_2) is False  # == False
    assert ingredient_2.__eq__(ingredient_3) is True  # == True
    assert ingredient_1.__repr__() == "Ingredient('queijo parmesão')"
    assert ingredient_1.name == "queijo parmesão"
    assert ingredient_2.name == "presunto"
    assert ingredient_1.restrictions == {Restriction.LACTOSE,
                                  Restriction.ANIMAL_DERIVED}
