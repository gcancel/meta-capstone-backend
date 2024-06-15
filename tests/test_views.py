from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer

class MenuViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.item_1 = Menu.objects.create(title='Cake', price=10, inventory=100)
        cls.item_2 = Menu.objects.create(title='Cheese', price=20, inventory=100)
    @classmethod
    def tearDownClass(cls):
        cls.item_1.delete()
        cls.item_2.delete()
    def test_getall(self):
        serialized = MenuSerializer(self.item_1)
        serialized_2 = MenuSerializer(self.item_2)
        
        self.assertEqual(serialized.data, {'title': 'Cake', 'price': '10.00', 'inventory': 100})
        self.assertEqual(serialized_2.data, {'title': 'Cheese', 'price': '20.00', 'inventory': 100})