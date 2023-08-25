import random

keys = ["C", "A", "G", "E", "D"]
positions = [1, 2, 3, 4, 5]
types = ["maj", "min"]
positions_to_intervals = {
  1: "1, 3, 5, 1, 3",
  2: "1, 5, 1, 3, 5",
  3: "1, 3, 5, 1, 3, 1",
  4: "1, 5, 1, 3, 5, 1",
  5: "1, 5, 1, 3"
}


def pick():
  random_key = random.choice(keys)
  random_position = random.choice(positions)
  random_type = random.choice(types)

  print("🎸 #" + str(random_position))
  input("🎼 " + random_key + " " + random_type)


def guess_intervals():
  random_position = random.choice(positions)
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
