import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.load_csv(source_path)

    def load_csv(self, source_path: str):
        make_dishes = {}
        with open(source_path, 'r') as file:
            reader = csv.reader(file)
            header, *data = reader

            for recipes in data:
                d_name, d_price, ingredient_name, ingredient_quantity = recipes

                if d_name in make_dishes:
                    dish = make_dishes[d_name]
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient_name),
                        int(ingredient_quantity)
                    )
                else:
                    dish = Dish(d_name, float(d_price))
                    make_dishes[d_name] = dish
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient_name),
                        int(ingredient_quantity)
                    )

        return list(make_dishes.values())
