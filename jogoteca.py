from flask import Flask, render_template

app = Flask(__name__)

class Jogos:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
a1 = Jogos("God of War","Hack n Slash","PS2")
a2 = Jogos("Lol","MOBA","PC")
a3 = Jogos("Batman","Ação e Aventura","PC/PS4/XBOX")
a4 = Jogos("CS:GO","FPS","PC")

lista = [a1,a2,a3,a4]

@app.route('/')
def ola():
    return render_template('lista.html',titulo='Jogos',jogos= lista)

@app.route('/novo')
def novo():
    return render_template('novo.html',titulo="titulo") 

@app.route('/criar')
def criar():
    return render_template('novo.html',titulo="titulo") 
app.run()