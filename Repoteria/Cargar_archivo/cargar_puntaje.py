class CargaArchivo:
  def cargar(self):
    import mysql.connector
    import pandas as pd
    import numpy as np
    import xlrd
    from pandas import ExcelWriter

    loc=("puntaje.xlsx")

    mydb = mysql.connector.connect(
      host='192.168.0.115',
      user='victor',
      password='192.168.1.2',
      database='test')

    mycursor = mydb.cursor()

    l=list()
    a = xlrd.open_workbook(loc)

    sheet=a.sheet_by_index(0)

    sheet.cell_value(0,0)

    for i in range(1,6):
      l.append(tuple(sheet.row_values(i)))

    sql = "REPLACE INTO puntuacion (hombres,mujeres,grupo) VALUES(%s,%s,%s)"
    mycursor.executemany(sql,l)

    mydb.commit()

    print(mycursor.rowcount, " datos cargados.")




    mycursor.execute("select hombres, mujeres, grupo from puntuacion")



    myresult = mycursor.fetchall()

    df=pd.DataFrame(myresult,
           columns = ['hombres','mujeres','grupo'])
    df.to_excel('Informe/Puntuacion.xlsx')

    print(df)
