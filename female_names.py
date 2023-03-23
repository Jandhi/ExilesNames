from names import prefix, female_suffix

from random import choice
for _ in range(20):
    name = choice(prefix) + choice(female_suffix)
    print(name.capitalize())