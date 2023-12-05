import psycopg2
import pandas


#connect to an existing DB
conn = psycopg2.connect(
    host="",
    database="scrap",
    user="postgres",
    password="Parisa4653")



#df = pandas.read_csv(r"C:\Users\PRS\Desktop\DBproject\scraper\whisky.csv")

cur = conn.cursor()
with open(r"C:\Users\PRS\Desktop\DBproject\scraper\whisky.csv") as f:
    next(f)
    cur.copy_from(f, 'product', sep=',')

    conn.commit()