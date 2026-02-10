from flask import Flask, request, render_template

app = Flask(__name__)

users = {"dan": "1234"}
print(users)
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
    name = request.form.get("name")
    senha = request.form.get("senha")
    users
    if name in users:
        return "Usuário já existe"

    users[name] = senha

    return "Conta criada! Agora faça login."

@app.route("/auth", methods=["POST"])
def auth():
    name = request.form.get("name")
    senha = request.form.get("senha")

    if name in users and users[name] == senha:
        return f"Welcome!, {name}"
    else:
        return "Login Wrong"
if __name__ == "__main__":
    app.run(debug=True)
