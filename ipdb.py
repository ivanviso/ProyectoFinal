import yaml
import sqlite3
import ipgen


with open(r'/home/ivan/ProyectoFinal/config.yaml') as config_file:
    config = yaml.safe_load(config_file)
    db_config=config["database"]

conn=sqlite3.connect(db_config["name"])
cursor = conn.cursor()
init=(f"""
    CREATE TABLE IF NOT EXISTS users (
	ip int UNIQUE,
   	user text PRIMARY KEY,
    wg_public_key text,
	asignado_en DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)     
cursor.execute(init)
conn.commit()
def nextip(network):
    UsedIPs=list()
    for ip in cursor.execute(f""" SELECT ip FROM users"""):
        UsedIPs.append(ip)
    return ipgen.ipgen(network,UsedIPs)
 
def sqlite(user):
    ip=nextip("10.10.0.0/16")
    cursor.execute(f""" REPLACE INTO users(ip,user,asignado_en) values({ip},"{user}",datetime())""")
    conn.commit()

for i in range(1000):
    sqlite(i)
    print(i)

for row in cursor.execute(f""" SELECT * FROM users"""):
    print(row)


#Falta la comprobación de asignación.