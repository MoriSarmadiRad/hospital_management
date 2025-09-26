from model.entity.admission.visit import Visit
from model.repository.repository import Repository


class VisitService :
    def __init__(self):
        self.repo = Repository(Visit)

    def save(self, visit):
        return self.repo.save(visit)

    def edit(self, visit):
        return self.repo.edit(visit)



