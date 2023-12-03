with open("input.txt", "r") as f:
    inp = f.read().splitlines()

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def first(str: str):
    index = 0
    for char in str:
        if char.isdigit():
            return char
        
        for i in range(index):
            substr = str[i:index+1]
            if digits.get(substr):
                return digits[substr]

        index += 1

def last(str: str):
    index = 0
    for char in str[::-1]:
        if char.isdigit():
            return char
        
        for i in range(index):
            if i > 0:
                substr = str[-index-1: -i]
            else:
                substr = str[-index-1:]
            if digits.get(substr):
                return digits[substr]

        index += 1


for string in inp:
    print(string, first(string), last(string))

print(sum([int(first(string) + last(string)) for string in inp ]))