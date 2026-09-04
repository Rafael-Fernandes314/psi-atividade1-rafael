from flask import Flask, request, render_template, session, redirect, url_for
import os
import models
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "batata")

@app.route("/")
def index():
    q = request.args.get("q")
    livros = models.buscar_livros(q)
    return render_template("index.html", livros=livros)

@app.route("/livro/<int:livro_id>")
def livro(livro_id):
    livro = models.buscar_livro(livro_id)
    if livro is None:
        return "Livro não encontrado", 404
    resenhas = models.resenhas_do_livro(livro_id)
    return render_template("livro.html", livro=livro, resenhas=resenhas)

@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        nome = request.form.get("nome","").strip()
        senha = request.form.get("senha","").strip()
        usuario_ok = None
        for usuario in models.usuarios:
            if usuario.get("nome") == nome and usuario.get("senha") == senha:
                usuario_ok = usuario
                break
        if usuario_ok:
            session["usuario"] = usuario_ok["nome"]
            return redirect(url_for("index"))
        erro = "nome ou senha inválidos"
    return render_template("login.html", erro=erro)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))