import pymysql
from openpyxl import load_workbook
db = pymysql.connect(host="localhost", user="root", password="yw980924@163.com", database="student_information")
cursor = db.cursor()
sqlDelete = "truncate table student_basic"
cursor.execute(sqlDelete)
filename = input("请拖入文件：")
wb = load_workbook(filename=filename)
sheetName = "学生"
ws = wb[sheetName]

for row in ws.rows:
    if row[0].value == "序号":
        continue
    else:
        name = row[3].value
        parentName = row[4].value
        parentNumber = row[5].value
        Grade = row[7].value
        Class = row[8].value
        Address = row[11].value
        SqlInsert = "INSERT INTO student_basic (studentname, grade, class, parentName_One, parentPhone_one, address) \
                    VALUES('%s', '%s', '%s','%s', '%s', '%s') " % \
                    (name, Grade, Class, parentName, parentNumber, Address)
        cursor.execute(SqlInsert)
        db.commit()

db.close()
