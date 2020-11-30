class Recipe:
    def __init__(self, recipe_cod, recipe_name, solid, liquid1, liquid2, powder, blend_time, id=None):
        self.id = id
        self.recipe_cod     = recipe_cod
        self.recipe_name    = recipe_name
        self.solid          = solid
        self.liquid1        = liquid1
        self.liquid2        = liquid2
        self.powder         = powder
        self.blend_time     = blend_time
