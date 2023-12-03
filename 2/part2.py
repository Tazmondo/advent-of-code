from functools import reduce


with open("input", "r") as f:
    inp = f.read().splitlines()

maxcolours = {
    "red": 12,
    "green": 13,
    "blue": 14
}

tot = 0

def line_possible(line: str):
    gamesplit = line.split(":")
    id = gamesplit[0][5:]

    contents = gamesplit[1].strip()
    rounds = contents.split(";")

    mincolours = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    for round in rounds:
        colours = round.split(",")
        for colour in colours:
            colour = colour.strip()
            for maxcolour in maxcolours.keys():
                if colour.endswith(maxcolour):
                    count = int(colour[:-len(maxcolour)-1])
                    mincolours[maxcolour] = max(count, mincolours[maxcolour])
    
            
    
    return reduce(lambda a, b: a * b, mincolours.values())

print(sum([line_possible(line) for line in inp]))