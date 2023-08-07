from random import randint
import os


def get_count(num: int, sec_num: int) -> int:
    return num + sec_num


def main():
    print("Введите по очереди два числа: ")
    print(get_count(int(input()), int(input())))


if __name__ == '__main__':
    main()
