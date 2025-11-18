from django.test import TestCase
from restaurant.models import MenuItem, Booking
from django.contrib.auth.models import User

class MenuItemViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.menu_item = MenuItem.objects.create(title='Pasta', price=12.99, inventory=10)
        self.menu_item = MenuItem.objects.create(title='Pizza', price=15.99, inventory=5)
        
    def test_getall(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    