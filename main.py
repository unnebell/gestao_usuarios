from flask import Flask

#inicialização
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    return "Olá, mundo!"

#execução
app.run(debug=True)