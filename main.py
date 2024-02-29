import sqlite3

# connecting to the database
connection = sqlite3.connect("gfg.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE Users ( 
userId INTEGER PRIMARY KEY, 
name VARCHAR(20), 
bio VARCHAR(30), 
researchField VARCHAR(30), 
posts INTEGER);
"""

sql_command_2 = """CREATE TABLE Post ( 
postId INTEGER PRIMARY KEY, 
title VARCHAR(20), 
datetime INTEGER);
"""

sql_command_3 = """CREATE TABLE Communities (
users VARCHAR(20),
posts VARCHAR(20));
"""

sql_drop_user_table = "DROP TABLE IF EXISTS Users;"
sql_drop_post_table = "DROP TABLE IF EXISTS Post;"
sql_drop_community_table = "DROP TABLE IF EXISTS Communities;"

crsr.execute(sql_drop_user_table)
crsr.execute(sql_drop_post_table)
crsr.execute(sql_drop_community_table)

# execute the statement
crsr.execute(sql_command)
crsr.execute(sql_command_2)
crsr.execute(sql_command_3)


# close the connection
connection.close()
