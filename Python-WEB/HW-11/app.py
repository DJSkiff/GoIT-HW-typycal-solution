from flask import Flask, appcontext_tearing_down, request, redirect, g


from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

from db_models import Note, Tag, get_session


app = Flask(__name__)
app.debug = True
app.env = 'development'

def get_session():
    engine = create_engine("sqlite:///mynotes.db")
    Session = sessionmaker(bind=engine)
    return Session()

def generate_tag_select():
    ses = get_session()
    result = ''
    tags = ses.query(Tag).all()
    for tag in tags:
        result += f'<option value="{tag.name}">{tag.name}</option>'
    print(result)
    return result

@app.route('/')
def index():
    ses = get_session()
    notes = ses.query(Note).all()

    result_html = '<form>'
    result_html += '<button><a href="/add_new/">Add "NOTE"</a></button>'
    result_html += '<button><a href="/add_tag/">Add "TAG"</a></button>'
    result_html += '<ul>'
    for rec in notes:
        if not rec.done:
            result_html += f'''<li>
            <a href="/detail/{rec.id}">
            {rec.name}</a>
            <a href="/done/{rec.id}">
            Make 'Done'</a>
            <a href="/delete/{rec.id}">
            Delete Note</a>
            </li>'''
        else:
            result_html += f'''<li><strike><a href="/detail/{rec.id}">{rec.name}</a></strike> </li>'''
    result_html += '</ul>'
    result_html += '</form>'
    return result_html


@app.route('/add_new/', methods=['GET', 'POST'])
def add_new():
    if request.method == 'POST':
        ses = get_session()
        name = request.form.get('name')
        description = request.form.get('description')
        tags = request.form.getlist('tags')
        tags_obj = []
        for tag in tags:
            tags_obj.append(ses.query(Tag).filter(Tag.name == tag).one())
        note = Note(name = name, description = description, tags = tags_obj)
        ses.add(note)
        ses.commit()
        return redirect('/')
    
    return '''<form method="POST">
                   <a href="/"> To "NOTES" </a>
                   <div style="padding:10px">
                        <label>Название заметки: 
                            <input type="text" name="name" required>
                        </label>
                    </div>
                   <div style="padding:10px">
                       <label>Описание: 
                           <input type="text" name="description" required>
                        </label>
                    </div>
                   <div style="padding:10px">
                       <label>Теги: 
                           <select type="" name="tags" multiple="multiple" required>'''\
                           + generate_tag_select()\
                     + ''' </select>
                       </label>
                    </div>
                   <input type="submit" value="Submit">
               </form>'''


@app.route('/detail/<id>')
def detail(id):
    ses = get_session()
    rec = ses.query(Note).filter(Note.id == id).first()
    result_html = '<form>'
    result_html += '<a href="/"> To "NOTES" </a>'
    result_html += f'<h1>{rec.name}</h1>'
    result_html += f'<div>Description: {rec.description}</div>'
    result_html += f'<div>Created: {rec.created.date()}</div>'
    result_html += f'<div>Выполнена: {"Да" if rec.done else "Нет"}</div>'
    result_html += f'<div>Теги: {rec.tags}</div>'
    result_html += '</form>'

    return result_html


@app.route('/delete/<id>')
def delete(id):
    ses = get_session()
    ses.query(Note).filter(Note.id == id).delete()
    ses.commit()

    return redirect('/')


@app.route('/done/<id>')
def done(id):
    ses = get_session()
    note = ses.query(Note).filter(Note.id == id).first()
    note.done = True
    ses.commit()

    return redirect('/')

@app.route('/add_tag/', methods=['GET', 'POST'])
def add_tag():
    if request.method == 'POST':
        ses = get_session()
        name = request.form.get('name')
        tag = Tag(name = name)
        ses.add(tag)
        ses.commit()
        return redirect('/')
    return '''<form method="POST">
                   <a href="/"> To "NOTES" </a>
                   <div style="padding:10px">
                        <label>Название тега: 
                            <input type="text" name="name" required>
                        </label>
                    </div>
                    <input type="submit" value="Submit">
              </form>'''


@appcontext_tearing_down
def close_connect(error):
    if hasattr()

if __name__ == '__main__':
    app.run()