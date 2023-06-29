from flask import flash, redirect, render_template, abort

from yacut import app, db
from .forms import LinkForm
from .models import URLMap


@app.route("/", methods=["GET", "POST"])
def index():
    form = LinkForm()
    if not form.validate_on_submit():
        return render_template("index.html", form=form)

    original = form.original_link.data
    render_date = dict(form=form, original=original)
    if form.custom_id.data:
        short = form.custom_id.data
        if URLMap.query.filter_by(short=short).first() is not None:
            flash(f"Имя {short} уже занято!", "short_error")
            return render_template("index.html", form=form)
        url = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        db.session.add(url)
        db.session.commit()
        return render_template("index.html", short=url.short, **render_date)

    url = URLMap.query.filter_by(original=original).first()
    if url is not None:
        return render_template("index.html", short=url.short, **render_date)

    url = URLMap(
        original=form.original_link.data,
    )
    db.session.add(url)
    db.session.commit()
    return render_template("index.html", short=url.short, **render_date)


@app.route("/<string:id>", methods=["GET"])
def redirection(id):
    url = URLMap.query.filter_by(short=id).first()
    if url is None:
        abort(404)
    return redirect(url.original), 302
