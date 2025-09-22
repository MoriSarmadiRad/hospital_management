from model.repository.repository import *
from model.entity.hos_dep.branch import *


class BranchService:
    def __init__(self):
        self.repo = Repository(Branch)


    def save(self, branch):
        return self.repo.save(branch)


    def edit(self, branch):
        return self.repo.edit(branch)


    def delete(self, branch_id):
        return self.repo.delete(branch_id)


    def find_by_branch_id(self, branch_id):
        return self.repo.find_by_id(branch_id)


    def find_all(self):
        return self.repo.find_all()