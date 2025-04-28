**Решение:**
```python
def calculate_grade(scores):
    average = round(sum(scores) / len(scores), 2)
    if average >= 4.5:
        return average, "Отлично"
    elif average >= 3.5:
        return average, "Хорошо"
    elif average >= 2.5:
        return average, "Удовлетворительно"
    else:
        return average, "Неудовлетворительно"
```
==================================
**Решение:**
```python
import random
import string

def generate_password(length=8):
    if length < 6:
        length = 6
    
    chars = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )
    
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if (
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*" for c in password) and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password)
        ):
            return password
```
