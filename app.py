# import the necessary packages
from flask import Flask, render_template, redirect, flash , url_for, request
import sys
import json
from flask_mysqldb import MySQL
import sqlite3
from datetime import datetime
from models.Recipe import Recipe
from models.Report import Report
from dao.RecipeDao import RecipeDao 
from dao.ReportDao import ReportDao
from pyModbusTCP.client import ModbusClient
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
import time


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["DEBUG"] = True

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("demo.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn

                                                    
@app.route('/relatorio')
def list_batch():
    db = db_connection()    
    reportDao = ReportDao(db)
    batchlist = reportDao.getReport()
    return render_template('report.html', titlePage='Relatório', batchs = batchlist)

# recipes functions
@app.route('/receitas')
def list_recipes():    
    db = db_connection()  
    recipeDao = RecipeDao(db)
    recipelist = recipeDao.getRecipes()
    return render_template('recipes.html', titlePage='Receitas', recipes=recipelist)

@app.route('/nova-receita')
def new_recipe():        
    return render_template('add_recipe_form.html', titlePage='Nova Receita')

@app.route('/adicionar-receita', methods=['POST'])
def add_recipe(): 
    db = db_connection()   
    recipe_cod  = request.form['recipe_cod']
    recipe_name = request.form['recipe_name']       
    solid       = request.form['solid']
    liquid1     = request.form['liquid1']
    liquid2     = request.form['liquid2']
    powder      = request.form['powder']
    blend_time  = request.form['blend_time']
    recipe      = Recipe(recipe_cod, recipe_name, solid, liquid1, liquid2, powder, blend_time)  
    recipeDao   = RecipeDao(db)
    recipeDao.addRecipe(recipe)               
    return redirect('receitas')

@app.route('/enviar-ihm/<int:id>')
def send_ihm(id):      
    return redirect(url_for('list_recipes'))   

@app.route('/editar-receita/<int:id>')
def edit_recipe(id): 
    db = db_connection()  
    recipeDao = RecipeDao(db)
    objId = recipeDao.getRecipeById(id)            
    return render_template('edit_recipe_form.html', titlePage='Editar Receita', recipe=objId)

@app.route('/atualizar-receita', methods=['POST',])
def update_recipe():  
    db = db_connection()  
    id = request.form['id']
    recipe_cod  = request.form['recipe_cod']
    recipe_name = request.form['recipe_name']
    solid       = request.form['solid']
    liquid1     = request.form['liquid1']
    liquid2     = request.form['liquid2']
    powder      = request.form['powder']
    blend_time  = request.form['blend_time']
    recipe      = Recipe(recipe_cod, recipe_name, solid, liquid1, liquid2, powder, blend_time, id=id) 
    recipeDao   = RecipeDao(db)
    updated     = recipeDao.updateRecipe(recipe)   
    return redirect('receitas')

@app.route('/remover-receita/<int:id>')
def delete_recipe(id):  
    db = db_connection()  
    recipeDao = RecipeDao(db)
    recipeDao.deleteRecipe(id)      
    return redirect(url_for('list_recipes'))     

@app.route('/')
def getData():    
    return render_template('dashboard.html', titlePage='Gráficos')

@app.route('/getAllRecipes', methods=['GET',])
def getAllRecipes():
    db = db_connection()  
    recipeDao = RecipeDao(db)
    recipelist = recipeDao.getRecipes()
    json_data=[]
    if len(recipelist):    
        row_headers = recipeDao.getRecipeHeaders()           
        for result in recipelist:  
            newlist = [str(i) for i in result]      
            json_data.append(dict(zip(row_headers,newlist)))
        return json.dumps(json_data)
    else:
        return json.dumps(json_data)


@app.route('/getAllReports', methods=['GET',])
def getAllReports():
    db = db_connection()  
    reportDao = ReportDao(db)    
    reportlist = reportDao.getReportByYear()    
    json_data=[]
    if len(reportlist):    
        row_headers = ["month","qty"]         
        for result in reportlist:  
            newlist = [str(i) for i in result]      
            json_data.append(dict(zip(row_headers,newlist)))
        return json.dumps(json_data)
    else: 
        return json.dumps(json_data)

  
if __name__ == "__manin__":
    app.run(debug=True)
