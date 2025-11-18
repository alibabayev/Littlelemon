from django.test import TestCase
from restaurant.models import Booking, MenuItem
from django.contrib.auth.models import User

class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    
    def test_get_item(self):
        item = MenuItem.objects.get(title="IceCream")
        self.assertEqual(str(item), "IceCream : 80.00")
        
class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(name="John Doe", no_of_guests=4, booking_date="2024-12-25")
    
    def test_get_booking(self):
        booking = Booking.objects.get(name="John Doe")
        self.assertEqual(str(booking), "John Doe - 2024-12-25")
        self.assertEqual(booking.no_of_guests, 4)
        self.assertEqual(str(booking.booking_date), "2024-12-25")