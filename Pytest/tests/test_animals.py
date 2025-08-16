from src.animals import Cat, Dog

import pytest



### FIXTURES ###

@pytest.fixture
def baseCat():
    return Cat()

@pytest.fixture
def baseDog():
    return Dog()

# a complex fixture calling other fixtures
@pytest.fixture
def animals(baseDog, baseCat):
    return [baseDog, baseCat]

### TESTS ###

# calls a simple fixture
def test_catMeows(baseCat):
    assert baseCat.speak() == "meow"
    
# calls a more complex fixture
def test_animalsSpeak(animals):
    for animal in animals:
        assert animal.speak() in ["meow", "bark"]

