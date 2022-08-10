from flask import Flask, render_template

app = Flask("hello")
nomeAula = "Aula python para Web"

@app.route("/usuario")
def usuario():
    usuario = [1, "Danilo de Souza Miguel", "Professor"]
    alunos = ["Andre Guedes", "Lucas Santos", "Alicia Duarte", "Raiane Caroline"]
    return render_template ("index.html", usuario=usuario, nome=nomeAula, alunos=alunos)

@app.route("/contatos")
def contato():
    return render_template("index.html", usuario=usuario, nome=nomeAula)