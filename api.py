from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
import psycopg2
import json

class Database:
 def __init__(self):
  self.conn = None

 def connect(self):
  if self.conn is None:
   try:
    self.conn = psycopg2.connect(database="????", user="postgres", password="????",host="localhost", port="5432")
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
 return '<h1>Test</h1>'


@app.route('/api/login', methods=['POST'])
def login():
    param=request.json
    username=param['username'];
    password=param['password'];
    str=f'SELECT public.login(\'{username}\',\'{password}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)



app.run()
print ("Operation done successfully");
conn.close()


