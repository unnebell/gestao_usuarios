# gestao_usuarios
Primeiros passos utilizando Framework Flask

# Estrutura
```
└── gestao_usuarios/
    ├── database/
    │   └── cliente.py
    ├── routes/
    │   ├── cliente.py
    │   └── home.py
    ├── static/
    │   ├── css/
    │   │   └── app.css
    │   └── js/
    │       └── cru.js
    ├── templates/
    │   ├── detalhe_cliente.html
    │   ├── form_cliente.html
    │   ├── index_cliente.html
    │   └── lista_clientes.html
    ├── main.py
    └── requirements.txt
```

### Install
```
$ python -m pip install -r requirements.txt
```

### Run
```
$ flask --app main run
```
