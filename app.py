from flask import Flask, render_template

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

if __name__ == '__main__':
  app.run()