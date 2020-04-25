# recursive function to move a tower from one location to another
def solve(height, location, destination):
    # assign the yet unused letter to side
    places = ["A", "B", "C"]
    del places[places.index(location)]
    del places[places.index(destination)]
    side = places[0]

    # going through every layer in the tower
    for n in range(height):
        # when the height is even, you start by placing a layer to the side
        if height % 2 == 0:
            value = n + 1
        # when the height is odd, you start by placing a layer to the destination
        else:
            value = n

        # since n is constantly being raised, this alternates between placing a layer to the side and to the destination
        if value % 2 == 0:
            yield location, destination
            # recursively execute this function again
            if n > 0:
                # yield everything from the new execution of this function
                for move in solve(n, side, destination):
                    yield move
        else:
            yield location, side
            if n > 0:
                for move in solve(n, destination, side):
                    yield move


if __name__ == "__main__":
    layers = int(input("How many layers: "))

    steps = 0
    for step in solve(layers, "A", "C"):
        print(f"{step[0]} {step[1]}")
        steps += 1
    print()
    print(f"steps: {steps}")
