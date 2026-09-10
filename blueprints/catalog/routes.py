from flask import request, render_template

from . import catalog_bp
import models

@catalog_bp.route("/")
def index():
    q = request.args.get("q")
    livros = models.buscar_livros(q)
    return render_template("index.html", livros=livros)
@catalog_bp.route("/livro/<int:livro_id>")
def livro(livro_id):
    livro = models.buscar_livro(livro_id)
    if livro is None:
        return "livro não encontrado", 404
    resenhas = models.resenhas_do_livro(livro_id)
    return render_template("livro.html", livro=livro, resenhas=resenhas)