from flask import Flask, render_template, request, redirect


from db import db_session
from models import Note, Tag


app = Flask(__name__)
app.debug = True
app.env = "development"


@app.route("/")
def index():
    # ses = get_session()
    notes = db_session.query(Note).all()
    return render_template("index.html", notes=notes)


@app.route("/detail/<id>")
def detail(id):
    note = db_session.query(Note).filter(Note.id == id).first()
    return render_template("detail.html", note=note)


@app.route("/add_note/", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        tags = request.form.getlist("tags")
        tags_obj = []
        for tag in tags:
            tags_obj.append(db_session.query(Tag).filter(Tag.name == tag).first())
        note = Note(name=name, description=description, tags=tags_obj)
        db_session.add(note)
        db_session.commit()
        return redirect("/")
    else:
        tags = db_session.query(Tag).all()

    return render_template("add_note.html", tags=tags)


@app.route("/add_tag/", methods=["GET", "POST"])
def add_tag():
    if request.method == "POST":
        name = request.form.get("name")
        tag = Tag(name=name)
        db_session.add(tag)
        db_session.commit()
        return redirect("/")

    return render_template("add_tag.html")


@app.route("/delete/<id>")
def delete(id):
    db_session.query(Note).filter(Note.id == id).delete()
    db_session.commit()

    return redirect("/")


@app.route("/done/<id>")
def done(id):
    db_session.query(Note).filter(Note.id == id).first().done = True
    db_session.commit()

    return redirect("/")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run()
