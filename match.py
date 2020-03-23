from Levenshtein import distance as levenshtein_distance
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('yubi')

args = parser.parse_args()

print('Comparing {} with volcanoes...'.format(args.yubi))

volcanoes = ''
with open('volcanoes', 'r') as volcanofile:
    volcanoes = volcanofile.read()
volcanoes = [_.lower() for _ in volcanoes.split()]

lowest = 1000000000
for v in volcanoes:
    dist = levenshtein_distance(args.yubi, v)
    if dist < lowest:
        best = v
        lowest = dist

print('{} is the most similar to {} with a distance of {}'.format(best, args.yubi, lowest))
