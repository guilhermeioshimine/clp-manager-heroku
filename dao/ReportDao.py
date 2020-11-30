from models.Report import Report

SQL_BY_ID = 'SELECT date, recipe_cod, recipe_name, solid, liquid1, liquid2, powder, blend_time from report where id = ?'
SQL_SELECT_ALL = 'SELECT * from report'
SQL_SELECT_YEAR = 'SELECT MONTH(date), COUNT(*) FROM report GROUP BY MONTH(date)'
SQL_ADD = 'INSERT into report (date, recipe_cod, recipe_name, solid, liquid1, liquid2, powder, blend_time) values (?, ?, ?, ?, ?, ?, ?, ?)'

class ReportDao():
    def __init__(self, db):
        self.__db = db

    def getReport(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_ALL)
        result = cursor.fetchall()                
        return result 
    
    def addReport(self, report):        
        cursor = self.__db.cursor()
        cursor.execute(SQL_ADD, (report.idRecipe, report.recipeDate, report.batch, report.solid, report.dosage1, report.dosage2, report.powder)) 
        self.__db.commit()               
        return report

    def getReportByYear(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_YEAR)
        result = cursor.fetchall()                
        return result

    def getReportHeaders(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_ALL)
        row_headers = [x[0] for x in cursor.description]
        return row_headers


