def move(location, destination):
    global count
    print(location + " " + destination)
    count = count + 1


def solve(number, location, destination):
    for letter in ["A", "B", "C"]:
        if letter not in location and letter not in destination:
            side = letter

    for n in range(number):
        if number % 2 == 0:
            value = n + 1
        else:
            value = n
        if value % 2 == 0:
            move(location, destination)
            if n > 0:
                solve(n, side, destination)
        else:
            move(location, side)
            if n > 0:
                solve(n, destination, side)


count = 0
solve(int(input("How many layers?")), "A", "C")
input(count)
