from flask import Flask, request
app = Flask(__name__)
import psycopg2
import json

class Database:
 def __init__(self):
  self.conn = None

 def connect(self):
  if self.conn is None:
   try:
    self.conn = psycopg2.connect(database="dadjoo", user="postgres", password="????",host="localhost", port="5432")
   except psycopg2.DatabaseError as e:
    print(e)

   def select_rows(self, query):
    self.connect()
    with self.conn.cursor() as cur:
     cur.execute(query)
     records = [row for row in cur.fetchall()]
     cur.close()
     return records

 def update_rows(self, query):
  self.connect()
  with self.conn.cursor() as cur:
   cur.execute(query)
   self.conn.commit()
   data = cur.fetchone()[0];
   cur.close()
   return data


@app.route('/')
def index():
 return '<h1>salam</h1>'
@app.route('/api/dadjoo_accept_expert', methods=['POST'])
def dadjoo_accept_expert():
    param=request.json
    expertid=param['expertid'];
    userid=param['userid'];
    str=f'SELECT public.dadjoo_accept_expert(\'{expertid}\',\'{userid}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)






