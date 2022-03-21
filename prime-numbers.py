import time

def get_prime_numbers(up_to_number):
    if up_to_number <= 0:
        print("Put number higher than 0.")
        return 0
    if up_to_number == 1:
        print("No prime numbers in this range.")
        return 1
    if up_to_number == 2:
        return {2}
    if up_to_number in (3, 4):
        return {2, 3}
    else:
        prime_numbers = {2, 3}
        odd_numbers = [number for number in range(5, up_to_number + 1)
                       if number % 2 != 0]
        for number in odd_numbers:
            divisions = 0
            for div_num in range(2, round(number / 3) + 1):
                if number % div_num == 0:
                    divisions += 1
                    break
            if not divisions:
                prime_numbers.add(number)

    return prime_numbers


def test_negative():
    result = get_prime_numbers(-3)
    assert result == 0


def test_zero():
    result = get_prime_numbers(0)
    assert result == 0


def test_one():
    result = get_prime_numbers(1)
    assert result == 1


def test_two():
    result = get_prime_numbers(2)
    assert len(result) == 1


def test_three():
    result = get_prime_numbers(3)
    assert len(result) == 2


def test_four():
    result = get_prime_numbers(4)
    assert len(result) == 2

def test_five():
    result = get_prime_numbers(5)
    assert len(result) == 3


def test_up_to_ten():
    result = get_prime_numbers(10)
    assert len(result) == 4


def test_up_to_twenty():
    result = get_prime_numbers(20)
    assert len(result) == 8


def test_up_to_fifty():
    result = get_prime_numbers(50)
    assert len(result) == 15


def test_up_to_hundred():
    result = get_prime_numbers(100)
    assert len(result) == 25


def test_up_to_thousand():
    result = get_prime_numbers(1000)
    assert len(result) == 168


def test_up_to_tenhousand():
    result = get_prime_numbers(10000)
    assert len(result) == 1229


def test_up_to_hunderthousand():
    start = time.time()
    result = get_prime_numbers(100000)
    end = time.time()
    print(end - start)
    assert len(result) == 9592


# def test_up_to_milion():
#     start = time.time()
#     result = get_prime_numbers(1000000)
#     end = time.time()
#     print(end - start)
#     assert len(result) == 78498
