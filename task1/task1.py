import argparse

parser = argparse.ArgumentParser(description='task1, circular array')
parser.add_argument('n', type=int, help='круговой массив')
parser.add_argument('m', type=int, help='интервал')
args = parser.parse_args()

task1_array = []
for i in range(1, args.n+1):
    task1_array.append(i)

n_array = task1_array
step = args.m - 1
value = n_array[step]
result = '1' + str(value)

while True:
    res = n_array[slice(step, len(n_array))] + n_array[slice(0, step)]
    value = res[step]
    result += str(value)
    n_array = res[slice(step, len(res))] + res[slice(0, step)]
    if value != 1:
        value = n_array[step]
        result += str(value)
        print(result)
    else:
        break

print(result)
