from flask import request, render_template, session, redirect, url_for

from . import auth_bp
import models

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        senha = request.form.get("senha", "").strip()
        usuario_ok = None
        for usuario in models.usuarios:
            if usuario.get("nome") == nome and usuario.get("senha") == senha:
                usuario_ok = usuario
                break
        if usuario_ok:
            session["usuario"] = usuario_ok["nome"]
            return redirect(url_for("catalog.index"))
        erro = "nome ou senha inválidos"
    return render_template("login.html", erro=erro)
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("catalog.index"))