import random

keys = ["C", "A", "G", "E", "D"]
positions = [1, 2, 3, 4, 5]
types = ["maj", "min"]
positions_to_intervals = {
    1: "1, 3, 5, 1, 3",
    2: "1, 5, 1, 3, 5",
    3: "1, 3, 5, 1, 3, 1",
    4: "1, 5, 1, 3, 5, 1",
    5: "1, 5, 1, 3",
}

def pick():
    random_key = random.choices(keys)[0]
    random_position = random.choices(positions)[0]
    random_type = random.choices(types)[0]

    print("🎸 #" + str(random_position))
    input("🎼 " + random_key + " " + random_type)


def guess_intervals():
    random_position = random.choices(positions)[0]
    intervals = positions_to_intervals[random_position]

    print("Position #?")
    print("🪜 " + intervals)
    guess = int(input("\n"))

    if guess == random_position:
        print('✅ correct!')
    else: 
        print('❌ wrong! guess again...\n')

        guess = int(input("\n"))
        if guess == random_position:
            print('✅ correct!')
        else:
            print('❌ wrong again! lets move on...')


def go():
    while True: 
        rand_num = random.random()
        if rand_num < 0.7:
            pick()
        else:
            guess_intervals()

        print('\n---\n')


go()

