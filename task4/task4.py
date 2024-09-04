import argparse

parser = argparse.ArgumentParser(description='task4, numbers')
parser.add_argument('numbers', help='массив целых чисел', type=argparse.FileType('r', encoding='UTF-8'))

args = parser.parse_args()

numbers = []
step = 0

for item in args.numbers.readlines():
    if '\n' in item:
        numbers.append(int(item[:-1]))
    else:
        numbers.append(int(item))
result = sum(numbers) // len(numbers)

while True:
    for number in numbers:
        if number < result:
            while number != result:
                number += 1
                step += 1
        elif number > result:
            while number != result:
                number -= 1
                step += 1
    else:
        break

print(step)
