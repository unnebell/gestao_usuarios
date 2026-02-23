from flask import Flask, url_for, render_template

#inicialização
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Fábio", "Cargo": True},
        {"nome": "Jordana", "Cargo": False},
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)


@app.route('/sobre')
def pagina_sobre():
    return """
        <b>Programador Python</b>
        <p>Testando criação de rotas</p>
    """

#execução
app.run(debug=True)