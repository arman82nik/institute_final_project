from model.repository import *
from model.tools.logging import Logger


connection_string = "sqlite:///model/repository/class_project.db"

if not database_exists(connection_string):
    create_database(connection_string)

engine=create_engine(connection_string, echo=False)

Session = sessionmaker(bind=engine)

base= Base()
base.metadata.create_all(bind=engine)
Logger.info("Database Created")


class Repository:
    def __init__(self, class_name):
        self.class_name = class_name

    def save(self, entity):
        session = Session()
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def edit(self, entity):
        session = Session()
        entity = session.merge(entity)
        session.commit()
        session.refresh(entity)
        return entity

    # def delete(self, entity):
    #     session = Session()
    #     session.add(entity)
    #     session.delete(entity)
    #     session.commit()

    def delete(self, entity_id):
        session = Session()
        entity = session.get(self.class_name, entity_id)
        session.delete(entity)
        session.commit()
        return entity

    def find_all(self):
        session = Session()
        return session.query(self.class_name).all()

    def find_by_id(self, entity_id):
        session = Session()
        return session.get(self.class_name, entity_id)

    def find_by(self, filter):
        session = Session()
        return session.query(self.class_name).filter(filter).all()


