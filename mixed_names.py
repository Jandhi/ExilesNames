from names import prefix, male_suffix, female_suffix

from random import choice
for _ in range(20):
    name = choice(prefix) + choice(choice((male_suffix, female_suffix)))
    print(name.capitalize())