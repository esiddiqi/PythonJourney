import random
dice_faces = [
'''
    ┌─────────┐
    │         │
    │    ●    │
    │         │
    └─────────┘
''',
'''
    ┌─────────┐
    │  ●      │
    │         │
    │      ●  │
    └─────────┘
''',

'''
    ┌─────────┐
    │  ●      │
    │    ●    │
    │      ●  │
    └─────────┘
''',

'''
    ┌─────────┐
    │  ●   ●  │
    │         │
    │  ●   ●  │
    └─────────┘
''',

'''
    ┌─────────┐
    │  ●   ●  │
    │    ●    │
    │  ●   ●  │
    └─────────┘
''',

'''    
    ┌─────────┐
    │  ●   ●  │
    │  ●   ●  │
    │  ●   ●  │
    └─────────┘
'''
]


# random_choice = random.shuffle(dice_faces)
# print(dice_faces[0])



def get_dice(num=2):
    for dice in range(0, num):
        print(random.choice(dice_faces))



