from random import randint
import os


def get_count(num: int, sec_num: int) -> int:
    return num + sec_num

def exist_count(res: int) -> bool:
    return isinstance(res, int)


def main():
    print("Введите по очереди два числа: ")
    res = get_count(int(input()), int(input()))
    print(res)
    print(exist_count(res))


if __name__ == '__main__':
    main()
