import json
from pprint import pprint
from sys import argv

class Food:
    def __init__(self, description, protein_val, caloric_val):
        self.description = description
        self.protein_val = protein_val # pro_units?
        eslf.caloric_val = caloric_val # cal_units?

def get_calories(food):
    for aspect in food['nutrients']:
        if aspect['description'] == 'Energy' and aspect['units'] == 'kcal':
            return aspect['value']

def get_protein(food):
    for aspect in food['nutrients']:
        if aspect['description'] == 'Protein':
            return aspect['value']

def find_above(min_ratio):

    with open('/Users/agata/Downloads/food.json') as file:
        foods = json.load(file)

    protein_val = 0
    caloric_val = 0

    protein_dict = {}
    for food in foods:
        caloric_val = get_calories(food)
        if caloric_val > 20:
            protein_val = get_protein(food)
            key = protein_val / caloric_val
            if key >= min_ratio:
                if key in protein_dict:
                    protein_dict[key].append(food)
                else:
                    protein_dict[key] = [food]

    return protein_dict

if __name__ == '__main__':
    min_ratio = 0.2
    protein_dict = find_above(min_ratio)
    ratios = protein_dict.keys()
    sorted_ratios = sorted(ratios, reverse=True)
    for ratio in sorted_ratios:
#        pprint(protein_dict[ratio])
        for food in protein_dict[ratio]:
            print(food['description'])
            for aspect in food['nutrients']:
                if aspect['description'] == 'Protein':
                    print(aspect['description'], end=" ")
                    print(aspect['value'], end=" ")
                    print(aspect['units'])
                else:
                    if aspect['description']=='Energy' and aspect['units']=='kcal':
                         print(aspect['description'], end=" ")
                         print(aspect['value'], end=" ")
                         print(aspect['units'])
                         print()
