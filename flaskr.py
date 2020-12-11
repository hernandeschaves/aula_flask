import sqlite3
from flask import Flask, render_template, request, g, redirect, url_for, \
    abort, session, flash

# Configuracoes
DATABASE = './tmp/flaskr.db'
USERNAME = 'admin'
PASSWORD = '123456'

# Criando o app
app = Flask(__mane__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def pos_requisicao():
    g.bd.close()

@app.route('/')
def exibir_entradas():
    sql = "select titulo, texto from entradas order by id desc"
    cursor = g.bd.execute()
    entradas = [dict(titulo=titulo, texto=texto) for titulo, texto in cursor.fetchall()]
    return render_template('exibir_entradas.html')

