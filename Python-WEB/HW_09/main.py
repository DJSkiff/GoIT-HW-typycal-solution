from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


from models import Note, Record, Tag


engine = create_engine("sqlite:///mynotes.db")
Session = sessionmaker(bind=engine)
session = Session()

tag1 = Tag(name="продукты")
tag2 = Tag(name="покупки")

note = Note(name="Сбегать в магазин")

note.tags = [tag1, tag2]

rec1 = Record(description="Купить хлеб", note=note)
rec2 = Record(description="Купить колбасу 0.5 кг", note=note)
rec3 = Record(description="Купить помидоры 1кг", note=note)

session.add(note)
session.commit()
