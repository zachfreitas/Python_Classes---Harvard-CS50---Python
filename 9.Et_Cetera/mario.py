import pandas as pd


def main():
    height = int(input("Height: "))
    pyramid(height)
    pass


def pyramid(n):
    for i in range(n):
        # print(i , end=" ")
        print("#" * (i + 1))
    pass


if __name__ == "__main__":
    main()
