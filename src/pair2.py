import json
from pprint import pprint
from sys import argv

def get_aspect(food, desc):
    for aspect in food['nutrients']:
        if aspect['description'] == desc:
            return aspect['value']

def find_above(min_ratio):

    with open('/Users/agata/Downloads/food.json') as file:
        foods = json.load(file)

    proteinval = 0
    caloricval = 0

    proteinarray = {}
    for food in foods:
        proteinval = get_aspect(food, 'Protein')
        caloricval = get_aspect(food, 'Energy')
        if caloricval > 10 and proteinval / caloricval >= min_ratio:
            key = proteinval / caloricval
            try:
                proteinarray[key].update(food)
            except KeyError:
                proteinarray.update({proteinval /caloricval : food}) 
    return proteinarray

min_ratio = 0.2
proteinarray = find_above(min_ratio)
ratios = proteinarray.keys()
sorted_ratios = sorted(ratios, reverse=True)

#s = "{:8f} {}".format(key, proteinarray[key]['description'])
input = argv[1]
if input in proteinarray.values():
    print('Good choice!')

#for key in sorted_ratios:
    #print("{:8f} {}".format(key, proteinarray[key]['description']))

#if __name__ == '__main__':
    #from sys import argv
    #found = find_above(float(argv[1]) if len(argv) > 1 else 0.2)
    #print(len(found))
    #for x in found:
        #print(x['description'])
