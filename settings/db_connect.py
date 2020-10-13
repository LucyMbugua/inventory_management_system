import psycopg2

# connect to a database
conn = psycopg2.connect(dbname="inventory_db", user="postgres", password="ADMIN")

