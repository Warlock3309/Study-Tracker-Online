from flask import Flask, request, render_template

app = Flask(__name__)

usuarios = {"daniel": "1234"}
print(usuarios)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login")
def login_page():
    return render_template("login.html")
@app.route("/create", methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    usuarios
    if nome in usuarios:
        return "Usuário já existe"

    usuarios[nome] = senha

    return "Conta criada! Agora faça login."

@app.route("/auth", methods=["POST"])
def auth():
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    if nome in usuarios and usuarios[nome] == senha:
        return f"Welcome!, {nome}"
    else:
        return "Login Wrong"
if __name__ == "__main__":
    app.run(debug=True)
