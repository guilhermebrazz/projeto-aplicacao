from models import db
from sqlalchemy.orm import sessionmaker

def usar_secao():

    try:

        Session = sessionmaker(bind=db) # Uma seção vinculada à minha database
        session = Session()

        yield session
            
    finally:  

        session.close()