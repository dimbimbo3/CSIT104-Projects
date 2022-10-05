def sum_series(x):
    total = 0
    for i in range(1, x+1):
        total += i/(i+1)
    return total

def main():
    x = 20
    for i in range(1, x+1):
       print(i, end = ' ')
       print(sum_series(i))

main()
