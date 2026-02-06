# tdd-fizz-buzz

A session on TDD with [Pytest](https://docs.pytest.org/en/7.4.x/)

Writing a function .fizz_buzz() that:

- Returns "Fizz 🍾" for numbers divisible by 3. 
- Returns "Buzz 🐝" for numbers divisible by 5. 
- Returns "FizzBuzz 🎉" for numbers divisible by both 3 and 5. 
- Returns the number itself for other numbers.

TDD must be used.

## To run code coverage reports

### Install coverage

```bash
pip install coverage
```

### Create coverage reports

```bash
coverage run -m pytest
```

### View coverage reports

```bash
coverage report
```
