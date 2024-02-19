from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import ProductCheckoutFactory


class CheckoutTestCase(APITestCase):
    def setUp(self):
        self.product_checkout_1 = ProductCheckoutFactory()
        self.product_checkout_2 = ProductCheckoutFactory()
        self.product_checkout_3 = ProductCheckoutFactory()

        self.order = [
            self.product_checkout_1,
            self.product_checkout_2,
            self.product_checkout_3
        ]

        self.session = self.client.session
        self.session['order'] = self.order
        self.session.save()

    def test_checkout_content_list_api_view(self):
        url = reverse("api:api_checkout_content")
        response = self.client.get(url)
        checkout_data = response.json()["checkout_content"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for checkout_product in checkout_data:
            self.assertIn('name', checkout_product)
            self.assertIn('price', checkout_product)
            self.assertIn('quantity', checkout_product)

            self.assertTrue(checkout_product['name'])
            self.assertTrue(checkout_product['price'])
            self.assertTrue(checkout_product['quantity'])

    def test_delete_all_products_api_view(self):
        url = reverse("api:api_checkout_delete_all")
        response = self.client.delete(url)

        self.assertDictEqual(
            {
                "message": "All products were removed from checkout."
            },
            response.json()
        )
        self.assertEqual(self.client.session.get("order"), [])

    def test_delete_checkout_api_view(self):
        url = reverse(
            "api:api_delete_product_in_checkout_from_checkout",
            kwargs={"product_id": self.product_checkout_1["product_id"]}
        )
        current_amount = len(self.client.session.get("order"))

        response = self.client.delete(url)
        updated_amount = len(self.client.session.get("order"))

        self.assertDictEqual(
            {
                "message": "Product removed from cart successfully."
            },
            response.json()
        )

        self.assertEqual(updated_amount, current_amount - 1)
