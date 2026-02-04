import random


def get_rand_number_list(amount: int) -> list[int]:
    try:
        number_list = list(range(1, amount + 1))
    except Exception as e:
        print(f"Imput amount invalid: {e}")
        return []
    random.shuffle(number_list)

    return number_list


def main():
    test1 = get_rand_number_list(10)
    test2 = get_rand_number_list(5)

    print("Randomized list 1:", test1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Randomized list 2:", test2)

if __name__ == "__main__":
    main()