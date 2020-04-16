import xlrd
import pymysql

from config.conf import *


def get_xlsx(row):
 exce=xlrd.open_workbook("../testdata/usermessage.xlsx")
 table=exce.sheets()[0]
 # print(table.nrows)
 # print(table.ncols)
 # print(table.row_values(0))#第一行
 # print(table.col_values(0))#第一列
 return table.cell_value(row,1),table.cell_value(row,2)
 # for x in range(1,table.nrows):
 #     print(table.cell_value(x,1),table.cell_value(x,2))

def get_mysql(sql):
    host,user,password,database,port,charset=sql_conf()
    db=pymysql.connect(host=host,user=user,password=password,database=database,port=port,charset=charset)
    cursor=db.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()
    cursor.close()
    db.close()
    return db
if __name__ == '__main__':
    get_xlsx()