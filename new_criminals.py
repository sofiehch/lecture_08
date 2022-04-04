import json


def main():
    names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
    production = [(138, 164, 151), (125, 113, 113), (52, 50, 63)]
    most_wanted = dict(zip(names, production))
    with open("new_criminals.json") as json_file:
        new_criminals = json.load(json_file)
    print(criminals(most_wanted, new_criminals))


def criminals(soucasny, novy):
    for key in novy:
        if key in soucasny.keys():
            soucasny[key] = novy[key]
        else:
            soucasny[key] = novy[key]
    return soucasny


if __name__ == '__main__':
    main()