TARGET = 2020

def part_one():
    cache = {}
    with open("input_01.txt") as f:
        for line in f:
            diff = TARGET - int(line)
            if diff in cache:
                print(f'{diff} x {line} = {diff * int(line)}')
                return
            cache[int(line)] = True


def part_two():
    with open("input_01.txt") as f:
        numbers = [int(line) for line in f.read().split('\n') if line != '']
        cache = {}
        for idx, n in enumerate(numbers):
            for m in numbers[idx+1:]:
                if TARGET - m in cache:
                    a, b = cache[TARGET - m]
                    print(f'{a} x {b} x {m} = {a * b * m}')
                    return
                cache[m+n] = (m, n)

def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
