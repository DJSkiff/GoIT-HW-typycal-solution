import configparser

from mongoengine import connect

from models import Note, Record, Tag

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('USER', 'user')
mongodb_pass = config.get('PASS', 'pass')
db_name = config.get('DB_NAME', 'db_name')

# connect to cluster on AtlasDB with connection string

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.onoag.mongodb.net/{db_name}?retryWrites=true&w=majority""", ssl=True, ssl_cert_reqs='CERT_NONE')

# count objects in collections
notes_count = Note.objects.count()

# if not objects in collections, create one
if not notes_count:
    # first - create Tag object
    tag = Tag(name='NewTag')
    # second - create Record object
    record = Record(description='NewRecordInNote')
    # and finally create Note object, and save it
    Note(name='MyFirstNote', records=[record, ], tags=[tag, ]).save()

# count objects again
notes_count = Note.objects.count()
print(notes_count)

# find object by name
note = Note.objects(name='NewNote1')

# if no object - create it
if not note:
    note = Note(name='NewNote1', records=[Record(description='NewNote'), ], tags=[Tag(name='NewNote'), ]).save()
else:
    # if the object exists - delete it
    note.delete()

# count objects again
notes_count = Note.objects.count()
print(notes_count)
