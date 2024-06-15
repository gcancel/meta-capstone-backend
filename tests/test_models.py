from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Ice Cream', price=80, inventory=100)
        self.assertEqual(f'{item.title}: {item.price}', 'Ice Cream: 80')