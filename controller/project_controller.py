from model.entity.project import Project
from model.service.project_service import ProjectService
from model.tools.decorators import exception_handling


class ProjectController:
    def __init__(self):
        self.service = ProjectService()

    @exception_handling
    def save(self, student_id, project_name, file_url, date_time, score):
        project = Project(student_id, project_name, file_url, date_time, score)
        return self.service.save(project)
