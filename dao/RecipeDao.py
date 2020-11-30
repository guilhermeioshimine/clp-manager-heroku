from models.Recipe import Recipe

SQL_DELETE = 'DELETE FROM recipe WHERE id = ?'
SQL_BY_ID = 'SELECT recipe_cod, recipe_name, solid, liquid1, liquid2, powder, blend_time from recipe where id = ?'
SQL_UPDATE = 'UPDATE recipe SET recipe_cod=?, recipe_name=?, solid=?, liquid1=?, liquid2=?, powder=?, blend_time=? WHERE id = ?'
SQL_SELECT_ALL = 'SELECT * from recipe'
SQL_ADD = 'INSERT into recipe (recipe_cod, recipe_name, solid, liquid1, liquid2, powder, blend_time) values (?, ?, ?, ?, ?, ?, ?)'

class RecipeDao:
    def __init__(self, db):
        self.__db = db

    def getRecipes(self):        
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_ALL)
        result = cursor.fetchall()                
        return result

    def getRecipeHeaders(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_ALL)
        row_headers=[x[0] for x in cursor.description]
        return row_headers

    def addRecipe(self, recipe):        
        cursor = self.__db.cursor()
        cursor.execute(SQL_ADD, (recipe.recipe_cod, recipe.recipe_name, recipe.solid, recipe.liquid1, recipe.liquid2, recipe.powder, recipe.blend_time)) 
        self.__db.commit()                   
        return recipe
    
    def getRecipeById(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BY_ID, (id,))
        obj = cursor.fetchone()
        return Recipe(obj[0], obj[1], obj[2], obj[3], obj[4],obj[5], obj[6], id)
    
    def updateRecipe(self, recipe):        
        cursor = self.__db.cursor()
        cursor.execute(SQL_UPDATE, (recipe.recipe_cod, recipe.recipe_name, recipe.solid, recipe.liquid1, recipe.liquid2, recipe.powder, recipe.blend_time, recipe.id))
        self.__db.commit()                       
        return recipe 
    
    def deleteRecipe(self, id):
        self.__db.cursor().execute(SQL_DELETE, (id,))
        self.__db.commit()     
