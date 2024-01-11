import mysql.connector
import json
from config import *

mydb = mysql.connector.connect(
  **ConfigDatabase
)

mycursor = mydb.cursor(buffered=True, dictionary=True)

def format_dict_values(dict_values):
    dict_values_format = {}
    for key in dict_values:
        if dict_values[key] == None:
            continue
        if key == "id":
            continue
        # check type dict, then convert to str json
        if type(dict_values[key]) == dict:
            dict_values_format[key] = json.dumps(dict_values[key])
        else:
            dict_values_format[key] = dict_values[key]

    return dict_values_format

def format_dict_wheres(dict_where):
    dict_where_format = {}
    for key in dict_where:
        if dict_where[key] == None:
            continue
        dict_where_format[str(key)] = dict_where[key]

    return dict_where_format

def auto_gen_sql_select(table_name, dict_where):
    sql = "SELECT * FROM " + table_name + " WHERE "
    for key in dict_where:
        sql += key + " = %s AND "
    sql = sql[:-5]

    return sql

def auto_gen_sql_insert(table_name, dict_values):
    sql = "INSERT INTO " + table_name + " ("
    for key in dict_values:
        sql += key + ", "
    sql = sql[:-2] + ") VALUES ("
    for key in dict_values:
        sql += "%s, "
    sql = sql[:-2] + ")"

    return sql

def auto_gen_sql_update(table_name, dict_values, dict_where):
    sql = "UPDATE " + table_name + " SET "
    for key in dict_values:
        sql += key + " = %s, "
    sql = sql[:-2] + " WHERE "
    for key in dict_where:
        sql += key + " = %s AND "
    sql = sql[:-5]

    return sql

def auto_gen_sql_delete(table_name, dict_where):
    sql = "DELETE FROM " + table_name + " WHERE "
    for key in dict_where:
        sql += key + " = %s AND "
    sql = sql[:-5]

    return sql

def sql_insert(table_name, dict_values):
    dict_values = format_dict_values(dict_values)
    values = tuple(dict_values.values())
    sql = auto_gen_sql_insert(table_name, dict_values)
    mycursor.execute(sql, values)
    mydb.commit()

    return mycursor.lastrowid

def sql_select(table_name, dict_where):
    dict_where = format_dict_wheres(dict_where)
    values = tuple(dict_where.values())
    sql = auto_gen_sql_select(table_name, dict_where)
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()

    return myresult

def sql_update(table_name, dict_values, dict_where):
    dict_values = format_dict_values(dict_values)
    dict_where = format_dict_wheres(dict_where)
    values = tuple(dict_values.values()) + tuple(dict_where.values())
    sql = auto_gen_sql_update(table_name, dict_values, dict_where)
    mycursor.execute(sql, values)
    mydb.commit()
    
    return mycursor.rowcount

def sql_delete(table_name, dict_where):
    dict_where = format_dict_wheres(dict_where)
    values = tuple(dict_where.values())
    sql = auto_gen_sql_delete(table_name, dict_where)
    mycursor.execute(sql, values)
    mydb.commit()

    return mycursor.rowcount