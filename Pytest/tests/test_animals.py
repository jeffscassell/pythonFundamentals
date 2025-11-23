import pytest

from packageName.animals import Cat, Dog



### FIXTURES ###

@pytest.fixture
def baseCat():
    return Cat()

@pytest.fixture
def baseDog():
    return Dog()

# A complex fixture calling other fixtures.
@pytest.fixture
def animals(baseDog, baseCat):
    return [baseDog, baseCat]

@pytest.fixture(params=(0,1,2))
def multiple(request):
    return request.param

### TESTS ###

# Calls a simple fixture.
def test_cat_meows(baseCat):
    assert baseCat.speak() == "meow"

# Calls a slightly more complex fixture.
def test_animals_speak(animals):
    for animal in animals:
        assert animal.speak() in ["meow", "bark"]

def test_raises_exception():
    with pytest.raises(OSError):
        raise OSError

# Creates 3 tests by itself due to the `multiple` fixture's multiple calls.
def test_multiple_calls(multiple):
    assert multiple in (0,1,2)
    # assert 0  # Will always fail the test, but allows us to see the value.
