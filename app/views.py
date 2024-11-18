from app import app
from flask import render_template, request, redirect, url_for
from app.models import cadastrar_usuario
from app.middleware.autenticacao import autenticar_usuario

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        if request.is_json:
            nome = request.json.get('nome')
            email = request.json.get('email')
            senha = request.json.get('senha')
            
        else:
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')
        
        print(nome, email, senha)
        response, status_code = cadastrar_usuario(nome, email, senha)
        if status_code == 400: 
            return render_template('cadastro.html', error=response['error'])
        elif status_code == 201:
            return redirect('/')
    
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = autenticar_usuario(email, senha)

        if usuario:
            return redirect('/')
        else:
            return render_template('login.html', error="Credenciais inválidas")
    
    return render_template('login.html')