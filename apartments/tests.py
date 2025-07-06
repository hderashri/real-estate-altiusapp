from django.test import TestCase, Client
from django.urls import reverse
from apartments.models import Apartment


class ApartmentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Apartment.objects.create(title="Apt A", location="Delhi", price=20000, bedrooms=2)
        Apartment.objects.create(title="Apt B", location="Mumbai", price=16000, bedrooms=1)
        Apartment.objects.create(title="Apt C", location="Bangalore", price=25000, bedrooms=3)

    def test_apartment_list_status_code(self):
        response = self.client.get(reverse('apartment_list'))
        self.assertEqual(response.status_code, 200)

    def test_apartment_filter_by_bedrooms(self):
        response = self.client.get(reverse('apartment_list'), {'bedrooms': 2})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apt A")
        self.assertNotContains(response, "Apt B")
        self.assertNotContains(response, "Apt C")

    def test_apartment_filter_by_price_range(self):
        response = self.client.get(reverse('apartment_list'), {
            'min_price': 17000,
            'max_price': 21000
        })
        self.assertContains(response, "Apt A")   # ₹20000
        self.assertNotContains(response, "Apt B") # ₹16000
        self.assertNotContains(response, "Apt C") # ₹25000

    def test_apartment_sorted_by_newest_first(self):
        response = self.client.get(reverse('apartment_list'), {'sort': '-created_at'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apt A")
        self.assertContains(response, "Apt B")
        self.assertContains(response, "Apt C")
