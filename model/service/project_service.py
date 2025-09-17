from model.repository.repository import *
from model.entity.project import Project



class ProjectService:
    def __init__(self):
        self.repository = Repository(Project)

    def save(self,project):
        return self.repository.save(project)


    def edit(self,project):
        return self.repository.edit(project)

    def delete(self,id):
        return self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self,id):
        return self.repository.find_by_id(id)






