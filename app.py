from var.data import data
from flask import *

app = Flask(__name__)
app.secret_key = '1234andi'

@app.errorhandler(404)
def err_handler(e):
  return render_template('404.html',
                         title=data['404']['title'],
                         sheets=data['404']['sheets'])

@app.route('/', defaults={'nom': 'Usuario'})
@app.route('/<nom>')
def index(nom):
  usuario = {}
  if 'user' in session:
    usuario = session['user']
  
  nombre = nom
  nombres = ['Andi', 'John', 'Luis']
  dic = {
    'names': ['John', 'Maria', 'Juan'],
    'ages': [25, 22, 21]
  }
  return render_template('index.html',
                         name=nombre,
                         names=nombres,
                         values=dic,
                         usuario=usuario,
                         title=data['index']['title'],
                         sheets=data['index']['sheets'])

@app.route('/clientes', defaults={'cli': 'Cliente 1', 'pro': 'Producto 1'})
@app.route('/clientes/<cli>/<pro>')
def clientes(cli, pro):
  cliente = cli
  producto = pro
  return render_template('clientes.html',
                         client=cliente,
                         product=producto,
                         title=data['clientes']['title'],
                         sheets=data['clientes']['sheets'])

@app.route('/register', methods=['GET', 'POST'])
def register():
  user = {
    'name': '',
    'email': ''
  }
  if request.args:
    user['name'] = request.args['nombre']
    user['email'] = request.args['correo']
    session['user'] = user
    return redirect('/')

  if request.method == 'POST':
    user['name'] = request.form['nombre']
    user['email'] = request.form['correo']
    session['user'] = user
    return redirect('/clientes')

  return render_template('register.html', usuario=user, title=data['register']['title'])

if __name__ == '__main__':
  app.run()