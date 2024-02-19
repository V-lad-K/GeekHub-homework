import factory
from products.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('name')
    price = factory.Faker('random_number', digits=2)
    short_description = factory.Faker('text')
    brand_name = factory.Faker('company')
    product_link = factory.Faker('url')
    product_id = factory.Sequence(lambda n: f'product_{n}')
    category_id = factory.SubFactory(CategoryFactory)


class ProductCheckoutFactory(factory.DictFactory):
    name = factory.Faker('name')
    price = factory.Faker('random_number', digits=2)
    quantity = factory.Faker('random_number', digits=2)
    product_id = factory.Sequence(lambda n: f'product_{n}')
