from django.test import TestCase
from restaurant.models import Menu  # Import the Menu model

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu1 = Menu.objects.create(title="Pizza", price=12.99, inventory=5)
        self.menu2 = Menu.objects.create(title="Burger", price=9.50, inventory=10)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('/your-view-url-here/')  # Replace with the actual view URL

        # Assert that the response is successful and contains the expected Menu objects
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['menu_list'], [
            repr(self.menu1),
            repr(self.menu2),
        ])
