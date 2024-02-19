from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import ProductFactory, CategoryFactory


class ProductTestCase(APITestCase):
    def setUp(self):
        self.category1 = CategoryFactory()
        self.category2 = CategoryFactory()

        self.product1 = ProductFactory(category_id=self.category1)
        self.product2 = ProductFactory(category_id=self.category2)
        self.product3 = ProductFactory(category_id=self.category1)
        self.product4 = ProductFactory(category_id=self.category2)
        self.product5 = ProductFactory(category_id=self.category1)
        self.product6 = ProductFactory(category_id=self.category2)

        print("self.product1 = ProductFactory(category_id=self.category1)", self.product1 )

    def test_product_detail_retrieve_api_view(self):
        url = reverse(
            "api:api_detail_products",
            kwargs={"product_id": self.product1.product_id}
        )
        response = self.client.get(url)
        product_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('name', product_data)
        self.assertIn('price', product_data)
        self.assertIn('product_id', product_data)

        self.assertTrue(product_data['name'])
        self.assertTrue(product_data['price'])
        self.assertTrue(product_data['short_description'])
        self.assertTrue(product_data['brand_name'])
        self.assertTrue(product_data['product_link'])
        self.assertTrue(product_data['product_id'])
        self.assertTrue(product_data['category_id'])

    def test_product_list_api_view(self):
        url = reverse("api:api_all_products")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('products', response.data)
        self.assertIn('categories', response.data)

        self.assertEqual(len(response.data['products']), 6)
        self.assertEqual(len(response.data['categories']), 2)

        for product_data in response.data['products']:
            self.assertIn('name', product_data)
            self.assertIn('price', product_data)
            self.assertIn('product_id', product_data)

            self.assertTrue(product_data['name'])
            self.assertTrue(product_data['price'])
            self.assertTrue(product_data['product_id'])

    def test_product_by_category_retrieve_api_view(self):
        url = reverse(
            'api:api_product_by_category',
            kwargs={'category_id': self.category1.id}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEquals(len(response.json()), 0)

        for product_data in response.json():
            self.assertIn('name', product_data)
            self.assertIn('price', product_data)
            self.assertIn('product_id', product_data)

            self.assertTrue(product_data['name'])
            self.assertTrue(product_data['price'])
            self.assertTrue(product_data['product_id'])
