body_structure_type = input()
animal_characteristic_type = input()
animal_food_type = input()

if body_structure_type == 'vertebrado':
    if animal_characteristic_type == 'ave':
        if animal_food_type == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if animal_food_type == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if animal_characteristic_type == 'inseto':
        if animal_food_type == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if animal_food_type == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
