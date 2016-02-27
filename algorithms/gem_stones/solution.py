def find_gemstones(rock, gemstones):
    difference = set()
    for element in gemstones:
        if not element in rock:
            difference.add(element)
    gemstones -= difference

t = int(input())

if t >= 1:
    rock = input()
    gemstones = set(rock)
    find_gemstones(rock, gemstones)

    for _ in range(t - 1):
        find_gemstones(input(), gemstones)

    print(len(gemstones))
