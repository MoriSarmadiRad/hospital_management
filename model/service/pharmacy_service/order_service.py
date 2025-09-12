from model.entity.pharmacy_entity.order import Order
from model.repository.repository import Repository

class OrderService:

    def __init__(self):
        self.repo = Repository(Order)

    def save(self,order):
        return self.repo.save(order)

    def edit(self,order):
        return self.repo.edit(order)

    def delete(self,id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_sample(self,sample):
        pass