from model.repository.repository import *
from model.entity.project import Project



class ProjectService:
    def __init__(self):
        self.repository = Repository(Project)

    def save(self,project):
        return self.repository.save(project)
