from model.entity.hos_dep.branch import Branch
from model.service.hos_dep_service import BranchService
from model.tools.decorators import exception_handling

class BranchController:
    def __init__(self):
        self.service = BranchService()

    @exception_handling
    def save (self,manajer,location,section):
        branch = Branch(manajer,location,section)
        return self.service.save(branch)

    @exception_handling
    def edit(self,branch_id,manajer,location,section):
        branch = Branch(manajer,location,section)
        branch.branch.id=branch_id
        return self.service.edit(branch)

    @exception_handling
    def delete(self,branch_id):
        return self.service.delete(branch_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_branch_id(self,branch_id):
        return self.service.find_by_branch_id(branch_id)








