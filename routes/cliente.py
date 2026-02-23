from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    #lista os clientes
    return render_template('lista_clientes.html')

@cliente_route.route('/', methods=['POST'])
def inserir_cliente(cliente_id):
    #inserir os dados do cliente no bd
    pass 

@cliente_route.route('/new')
def form_cliente():
    #formulário para cadastrar um cliente
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template("detalhe_cliente.html")

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    #formulario para editar um cliente
    return render_template("form_edit_cliente.html")

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    #atualizar as informações de um cliente
    pass 

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    #apaga o registro de um cliente
    pass 