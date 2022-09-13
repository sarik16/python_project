import cx_oracle

try:
    #create connection
      conn = cx_oracle.connect('system/system@//localhost:1521/orcl')
except exception as err:
    print('error connection')
else
     print(conn.varsion)
     try:
         # create cursor
         cur = conn.cursor()
         sql_create =(" CREATE TABLE NUMBER_PLT(
         ID INT PRIMARY KEY,
         V_NO VARCHAR(10)
         )")
         cur.execute(sql_create)
     except exception as err:
         print('error table creation')
     else
         print('table created')
         try:
             # create cursor
             cur = conn.cursor()
             sql_insert = (" INSERT INTO NUMBER_PLT VALUES(text)")
             cur.execute(sql_insert)
         except exception as err:
             print('error insert')
         else
             print('inserted')
finally:
    cur.close()
    conn.close()

