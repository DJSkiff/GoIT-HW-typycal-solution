import configparser

from mongoengine import connect

from models import Note, Record, Tag

config = configparser.ConfigParser()
config.read('config.ini')

mongodb_pass = config.get('PASS', 'pass')

connect(host=f"mongodb+srv://dev:{mongodb_pass}@cluster0.onoag.mongodb.net/Notes?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs = "CERT_NONE")

tag = Tag(name = 'food')

notes = Note.objects()

for note in notes:
   if tag in note.tags:
       print(note)