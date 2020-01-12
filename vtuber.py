# coding: utf-8
import pyodbc
import struct
import datetime
import constant
from vtubers import Vtubers

server = constant.DB_SERVER
database = constant.DB_NAME
username = constant.DB_USER
password = constant.DB_PASSWORD

<<<<<<< HEAD
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
=======
cnxn = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
>>>>>>> origin/master

def handle_datetimeoffset(dto_value):
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 0, -6, 0)
    tweaked = [tup[i] // 100 if i == 6 else tup[i] for i in range(len(tup))]
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:07d} {:+03d}:{:02d}".format(*tweaked)

cursor = cnxn.cursor()
cnxn.add_output_converter(-155, handle_datetimeoffset)

SELECT_ALL_SQL = 'SELECT * FROM vtubers'
UPDATE_SQL = "UPDATE vtubers SET updated_at = '{updated_at}' WHERE vtuber_id = {vtuber_id}"

class Vtuber():
    def find_all(self):
        vtubers = []
        with cursor.execute(SELECT_ALL_SQL):
            row = cursor.fetchone()
            while row:
                vtuber = Vtubers()
                vtuber.vtuber_id = row[0]
                vtuber.name = row[1]
                vtuber.channel_id = row[2]
                vtuber.channel_title = row[3]
                vtuber.calendar_id = row[4]
                updated_at = datetime.datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f0 %z')
                vtuber.updated_at = updated_at
                vtubers.append(vtuber)
                row = cursor.fetchone()
        return vtubers
    
    def update(self, vtuber):
        edit_sql = UPDATE_SQL.replace('{updated_at}', vtuber.updated_at)
        edit_sql = edit_sql.replace('{vtuber_id}', str(vtuber.vtuber_id))
        cursor.execute(edit_sql)
        cursor.commit()
        return