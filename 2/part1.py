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

    possible = True

    for round in rounds:
        if not possible:
            break

        colours = round.split(",")
        for colour in colours:
            colour = colour.strip()
            for maxcolour in maxcolours.keys():
                if colour.endswith(maxcolour):
                    if int(colour[:-len(maxcolour)-1]) > maxcolours[maxcolour]:
                        possible = False
                        break
    
    if possible:
        return int(id)
    else:
        return 0

print(sum([line_possible(line) for line in inp]))