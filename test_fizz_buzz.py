from fizz_buzz import fizz_buzz

def test_just_number():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(19) == 19

def test_fizz():
    assert fizz_buzz(3) == "Fizz 🍾"
    assert fizz_buzz(6) == "Fizz 🍾"

def test_buzz():
    assert fizz_buzz(5) == "Buzz 🐝"

def test_fizz_buzz():
    assert fizz_buzz(15) == "FizzBuzz 🎉"
    #assert fizz_buzz(3) == "Fizz"   