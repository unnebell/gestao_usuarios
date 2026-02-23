from flask import Flask, url_for

#inicialização
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    return f"<a href='{url_for('pagina_sobre')}'>Página sobre</a>"

@app.route('/sobre')
def pagina_sobre():
    return """
        <b>Programador Python</b>
        <p>Testando criação de rotas</p>
    """

#execução
app.run(debug=True)