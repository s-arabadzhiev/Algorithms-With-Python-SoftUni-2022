
def print_fig(n):
    if n == 0:
        return

    print("*" * n)
    print_fig(n - 1)
    print("#" * n)


rows = int(input())
print_fig(rows)
