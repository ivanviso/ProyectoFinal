import yaml

with open(r'/home/ivan/ProyectoFinal/config.yaml') as config_file:
    config = yaml.safe_load(config_file)
    db_config=config["database"]
    print(db_config)



def sqlite():
    import sqlite3
    
    conn=sqlite3.connect(db_config["name"])
    cursor = conn.cursor()
    init=("""
    CREATE TABLE IF NOT EXISTS {}users (
	ip int UNIQUE ,
   	user varchar(64) PRIMARY KEY,
	asignado_en DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """).format(db_config["prefix"])
    cursor.execute(init)
    cursor.execute(""" replace into users(ip,user,asignado_en) values(232,"i22v2an",datetime())""")
    cursor.execute(""" SELECT * FROM users""")
    conn.commit()
    print(cursor.fetchall())
sqlite()