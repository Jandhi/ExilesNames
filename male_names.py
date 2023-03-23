from names import prefix, male_suffix

from random import choice
for _ in range(20):
    name = choice(prefix) + choice(male_suffix)
    print(name.capitalize())