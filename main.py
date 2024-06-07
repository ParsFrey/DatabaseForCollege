#classes1,2 : 
#students ali,mamad,rose,ana :
#proffesors samiee,hesabi :
#engine_building :
#art_building :
#days such as saturday, sunday, monday,tuesday, wednesday,thursday,friday (and their times):
# WE DIDN'T USE PRIMARY KEY FOR THIS ONE BECAUSE ALL THE INFORMATION ARE CONNECTED TO EACH OTHER.
import sqlite3
conn = sqlite3.connect("College_Management")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS saturday (       
    class_time TEXT NOT NULL,
    class_id INTEGER,
    proffesor_name TEXT,
    building_name TEXT,
    student_name TEXT               
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS sunday (
    class_time TEXT NOT NULL,
    class_id INTEGER,
    proffesor_name TEXT,               
    building_name TEXT,               
    student_name TEXT               
                                    
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS monday (      
    class_time TEXT NOT NULL,
    class_id INTEGER,
    proffesor_name TEXT,               
    building_name TEXT,              
    student_name TEXT               
                                     
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS tuesday (      
    class_time TEXT NOT NULL,
    class_id INTEGER,
    proffesor_name TEXT,               
    building_name TEXT,             
    student_name TEXT               
                                     
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS wednesday (      
    class_time TEXT NOT NULL,
    class_id INTEGER,
    proffesor_name TEXT,               
    building_name TEXT,             
    student_name TEXT               
                                     
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS thursday (      
    class_time TEXT NOT NULL,
    class_id INTEGER,
    proffesor_name TEXT,               
    building_name TEXT,              
    student_name TEXT               
                                    
)
''')
conn.commit()
conn.close()