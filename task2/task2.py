import argparse

parser = argparse.ArgumentParser(description='task2, circle')
parser.add_argument('circle_file', help='координаты центра окружности и радиус', type=argparse.FileType('r', encoding='UTF-8'))
parser.add_argument('dots_file', help='координаты точек', type=argparse.FileType('r', encoding='UTF-8'))
args = parser.parse_args()

circle = []
dots = []
for item in args.circle_file.readlines():
    if '\n' in item:
        circle.append(item[:-1])
    else:
        circle.append(item)
for item in args.dots_file.readlines():
    if '\n' in item:
        dots.append(item[:-1])
    else:
        dots.append(item)

x_center = int(circle[0].split(' ')[0])
y_center = int(circle[0].split(' ')[-1])
radius = int(circle[1])

for dot in dots:
    if (int(dot.split(' ')[0]) - x_center)  ** 2 + (int(dot.split(' ')[-1]) - y_center) ** 2 < radius ** 2:
        print(1)
    elif (int(dot.split(' ')[0]) - x_center)  ** 2 + (int(dot.split(' ')[-1]) - y_center) ** 2 == radius ** 2:
        print(0)
    else:
        print(2)
