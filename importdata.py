import pymysql
from openpyxl import load_workbook
db = pymysql.connect(host="localhost", user="root", password="yw980924@163.com", database="student_information")
cursor = db.cursor()
filename = input("请拖入文件：")
wb = load_workbook(filename=filename)
sheetName = "学生"
ws = wb[sheetName]

for row in ws.rows:
    if ws.cell(row, 1).value == "序号":
        continue
    else:
        name = row[4].value
        parentName = row[5].value
        parentNumber = row[6].value
        Grade = row[8].value
        Class = row[9].value
        Address = row[12].value
        SqlInsert = "INSERT INTO student_basic (studentname, grade, class, parentName_One, parentPhone_one, address) \
                    VALUES('%s', '%s', '%s','%s', '%s', '%s') " % \
                    (name, Grade, Class, parentName, parentNumber, Address)
        cursor.execute(SqlInsert)
        db.commit()

db.close()