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

    @exception_handling
    def edit(self, id, student_id, project_name, file_url, date_time, score):
        project = Project(id,student_id, project_name, file_url, date_time, score)
        project.id = id
        return self.service.edit(project)

    def delete(self, id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"error: {e}"

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"

    def find_by_id(self, id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"error: {e}"


