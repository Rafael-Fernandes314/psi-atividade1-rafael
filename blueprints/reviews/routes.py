from flask import redirect, request, session, url_for

from . import reviews_bp
import models

@reviews_bp.route("/livro/<int:livro_id>/resenhar", methods=["POST"])
def resenhar(livro_id):
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    texto = request.form.get("texto", "").strip()
    nota = request.form.get("nota", "0")

    if not texto or not nota.isdigit():
        return redirect(url_for("catalog.livro", livro_id=livro_id))

    nota = int(nota)
    if nota < 1 or nota > 5:
        return redirect(url_for("catalog.livro", livro_id=livro_id))

    models.resenhas.append({
        "id": models.proximo_id_resenha,
        "livro_id": livro_id,
        "usuario": session["usuario"],
        "texto": texto,
        "nota": nota,
    })
    models.proximo_id_resenha += 1
    return redirect(url_for("catalog.livro", livro_id=livro_id))
