def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"{n}:{source}->{target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"{n}:{source}->{target}")
    hanoi(n - 1, auxiliary, target, source)

n = int(input())
hanoi(n, 'A', 'C', 'B')
