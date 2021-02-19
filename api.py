from flask import Flask, request
from flask_cors import CORS
import psycopg2
import json

ROOM = 'room'
from flask_socketio import SocketIO,join_room, leave_room

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

class Database:
 def __init__(self):
  self.conn = None

 def connect(self):
  if self.conn is None:
   try:
    self.conn = psycopg2.connect(database="dadjoo8", user="postgres", password="Navid16110202*",host="localhost", port="5432")
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


@app.route('/api/dadjoo_add_freetime', methods=['GET ','POST'])
def dadjoo_add_freetime():
    param=request.json
    d=json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_add_freetime(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_delete_freetime', methods=['GET ','POST'])
def dadjoo_delete_freetime():
    param=request.json
    d=json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_delete_freetime(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_get_list_of_freetime', methods=['GET','POST'])
def dadjoo_get_list_of_freetime():
    param=request.json
    d = json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_get_list_of_freetime(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_insert_file', methods=['GET','POST'])
def dadjoo_insert_file():
    param=request.json
    d=json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_insert_file(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_insert_listfile', methods=['GET','POST'])
def dadjoo_insert_listfile():
    param=request.json
    d = json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_insert_listfile(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_login', methods=['POST'])
def dadjoo_login():
    param=request.json
    tusername=param['tusername'];
    tpass=param['tpass'];
    str=f'SELECT public.dadjoo_login(\'{tusername}\',\'{tpass}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_reg_client', methods=['GET ','POST'])
def dadjoo_reg_client():
    param=request.json
    d=json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_reg_client(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_reg_expert', methods=['GET','POST'])
def dadjoo_reg_expert():
    param=request.json
    d=json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_reg_expert(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_send_message', methods=['GET','POST'])
def dadjoo_send_message():
    param=request.json
    d = json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_send_message(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


# @app.route('/api/dadjoo_specialty_list', methods=['GET','POST'])
# def dadjoo_get_client_info():
#     str=f'SELECT public.dadjoo_specialty_list(\'\');';
#     db = Database()
#     data = db.update_rows(str)
#     y = json.dumps(data)
#     return(y)


@app.route('/api/dadjoo_update_freetime', methods=['GET ','POST'])
def dadjoo_update_freetime():
    param=request.json
    d=json.dumps(param['intext'])
    str=f'SELECT public.adjoo_update_freetime(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_get_client_info', methods=['GET','POST'])
def dadjoo_get_client_info():
    param=request.json
    d = json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_get_client_info(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@app.route('/api/dadjoo_search_expert', methods=['GET','POST'])
def dadjoo_search_expert():
    param=request.json
    d=json.dumps(param['intext'])
    str=f'SELECT public.dadjoo_search_expert(\'{d}\');';
    db = Database()
    data = db.update_rows(str)
    y = json.dumps(data)
    return(y)


@socketio.on('connect')
def connect():
    socketio.emit('ready', room=ROOM, skip_sid=request.sid)
    join_room(ROOM)


@socketio.on('disconnect')
def disconnect():
    leave_room(ROOM)


@socketio.on('data')
def data(data):
    if data :
      socketio.emit('data', data, room=ROOM,skip_sid=request.sid)


socketio.run(app)
print ("Operation done successfully");
conn.close()


