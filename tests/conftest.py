from pytest_factoryboy import register

from factories import AdFactory, CategoryFactory, UserFactory

pytest_plugins = "tests.fixtures"


register(AdFactory)
register(CategoryFactory)
register(UserFactory)
