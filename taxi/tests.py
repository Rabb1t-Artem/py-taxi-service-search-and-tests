from django.test import TestCase
from django.urls import reverse_lazy
from taxi.forms import DriverCreationForm


class CreateTest(TestCase):
    def test_car_search(self):
        data = {
            "model": "F",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:car-list"), data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "model")
        self.assertContains(response, "page")

    def test_driver_search(self):
        data = {
            "username": "A",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:driver-list"), data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "username")
        self.assertContains(response, "page")

    def test_manufacturer_search(self):
        data = {
            "name": "T",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:manufacturer-list"), data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertContains(response, "page")


class TestDriverCreationForm(TestCase):
    def test_driver_creation_form_with_license_number_first_name_and_last_name(
        self,
    ):
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "license_number": "JOY26458",
            "first_name": "John",
            "last_name": "Doe",
        }

        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
