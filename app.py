from flask import Flask, render_template, request

app = Flask(__name__)

@app.errorhandler(404)
def err_handler(e):
  return render_template('404.html')

@app.route('/', defaults={'nom': 'Usuario'})
@app.route('/<nom>')
def index(nom):
  nombre = nom
  nombres = ['Andi', 'John', 'Luis']
  dic = {
    'names': ['John', 'Maria', 'Juan'],
    'ages': [25, 22, 21]
  }
  return render_template('index.html', name=nombre, names=nombres, values=dic)

@app.route('/clientes', defaults={'cli': 'Cliente 1', 'pro': 'Producto 1'})
@app.route('/clientes/<cli>/<pro>')
def clientes(cli, pro):
  cliente = cli
  producto = pro
  return render_template('clientes.html', client=cliente, product=producto)

@app.route('/register', methods=['GET', 'POST'])
def register():
  user = {
    'name': '',
    'email': ''
  }
  if request.args:
    user['name'] = request.args['nombre']
    user['email'] = request.args['correo']

  if request.method == 'POST':
    user['name'] = request.form['nombre']
    user['email'] = request.form['correo']

  return render_template('register.html', usuario=user)

if __name__ == '__main__':
  app.run()