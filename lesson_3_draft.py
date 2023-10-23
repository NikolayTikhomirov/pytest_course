import pytest

@pytest.fixture
def setup_teardown():
    # Код предусловия (setup)
    print("\nПредусловие")
    yield
    # Код постусловия (teardown)
    print("\nПостусловие")


def test_example(setup_teardown):
    # Код теста
    print("\nТест")
