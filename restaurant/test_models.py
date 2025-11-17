from django.test import TestCase
from restaurant.models import Booking, MenuItem
from django.contrib.auth.models import User

class MenuItemModelTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Test Dish", price=9.99, inventory=10)
    
    def test_get_item(self):
        item = MenuItem.objects.get(title="Test Dish")
        self.assertEqual(str(item), "Test Dish")
        self.assertEqual(item.price, 9.99)
        self.assertEqual(item.inventory, 10)
        
class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(name="John Doe", no_of_guests=4, booking_date="2024-12-25")
    
    def test_get_booking(self):
        booking = Booking.objects.get(name="John Doe")
        self.assertEqual(str(booking), "John Doe - 2024-12-25")
        self.assertEqual(booking.no_of_guests, 4)
        self.assertEqual(str(booking.booking_date), "2024-12-25")