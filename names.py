prefix = [
    'ael',
    'aelf',
    'ald',
    'alt',
    'an',

    'bair',
    'bed',
    'bel',

    'cat',
    'cath',

    'eber',
    'em',

    'ffar',

    'gala',
    'gar',
    'geir',
    'gwen',
    'gwyn',
    'goth',
    'grim',

    'llan',
    'lion',
    'luc',
    'lun',
    'lyn',

    'mad',
    'merch',
    'murk',
    'mor',

    'ober',
    'o',
    'or',

    'pell',
    'pryd',

    'rhi',
    'rhaeg',
    'rhod',

    'sag',

    'wyn',
]

male_suffix = [
    'ac',
    'an',
    'ar',

    'bald',
    'bard',
    'bolt',
    
    'cain',

    'el',
    'eth',

    'din',
    'dred',

    'frey',
    'frid',

    'gain',
    'goth',
    
    'had',
    'hart',

    'in',

    'ley',
    'lin',
    
    'mar',
    'more',
    'mond',

    'och',
    
    'ras',
    'ric',
    'r',
    
    'was',
    'wain',
    'wen',
    'wyr',
]

female_suffix = [
    'a',
    'ara',
    'aela',

    'dine',

    'ed',
    'elle',
    'ene',

    'gana',
    'gaine',

    'ian',
    'ine',
    'inore',

    'lain',
    'lia',

    'rid',
    'rys',

    'wyn',
    'were',
    
    'yd',
    'ys',
    'yth',
]

from random import choice
for _ in range(20):
    name = choice(prefix) + choice(female_suffix)
    print(name.capitalize())