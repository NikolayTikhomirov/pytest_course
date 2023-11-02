from faker import Faker 
import pytest
from registration.conftest import driver, options, wait


@pytest.fixture
def random_email():
    faker = Faker()
    return faker.email()


