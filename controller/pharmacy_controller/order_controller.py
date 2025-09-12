from model.entity.pharmacy_entity.order import Order
from model.service.pharmacy_service.order_service import OrderService
from model.tools.decorators import exception_handling


class OrderController:
    def __init__(self):
        self.service = OrderService()