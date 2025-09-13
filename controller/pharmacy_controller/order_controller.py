from model.entity.pharmacy_entity.order import Order
from model.service.pharmacy_service.order_service import OrderService
from model.tools.decorators import exception_handling


class OrderController:
    def __init__(self):
        self.service = OrderService()

    @exception_handling
    def save(self,prescription_id, payment_num, drug_id, employee_id,order_date,total_amount, description):
        order=Order(prescription_id, payment_num, drug_id, employee_id,order_date,total_amount, description)
        return self.service.save(order)

    @exception_handling
    def edit(self,order_id,prescription_id, payment_num, drug_id, employee_id,order_date,total_amount, description):
        order = Order(prescription_id, payment_num, drug_id, employee_id,order_date,total_amount, description)
        order.order_id = order_id
        return self.service.edit(order)

    @exception_handling
    def delete(self, order_id):
        return self.service.delete(order_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_order_id(self, order_id):
        return self.service.find_by_id(order_id)