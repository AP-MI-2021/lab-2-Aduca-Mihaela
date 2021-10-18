def print_menu():
    print("1. Verifica daca un numar este prim.")
    print("2. Verifica daca un numar este palindrom.")
    print("3. Iesire.")


def is_prime(n):
    """
    Verifica daca un numar este prim sau nu.
    :param n:numar natural
    :return:Returneaza True daca un numar este prim si False in caz contrar.
    """
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    """
    Gaseste un nr prim mai mic decat un numar dat.
    :param n: nr intreg
    :return:un nr prim mai mic decat un numar dat.
    """
    nr_prim = n - 1
    ok = False
    if n <= 2:
        return None
    while not ok:
        if is_prime(nr_prim):
            ok = True
            break
        nr_prim = nr_prim - 1
    return nr_prim


def test_get_largest_prime_below():
    assert get_largest_prime_below(36) == 31
    assert get_largest_prime_below(135) == 131
    assert get_largest_prime_below(76) == 73

def is_palindrome(n):
    """
    Verifica daca un numar dat este palindrom sau nu.
    :param n: intreg
    :return: Returneaza True daca numarul n este palindrom, sau va returna False in caz contrar.
    """
    ogl = 0
    x = n
    while x != 0:
        ogl = ogl * 10 + x % 10
        x = x // 10
    if ogl == n:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(717) == True
    assert is_palindrome(9807) == False
    assert is_palindrome(10401) == True


def main():
    test_get_largest_prime_below()
    test_is_palindrome()

    while True:
        print_menu()
        optiune = input("Dati optiunea:")

        if optiune == "1":
            numar=int(input("Dati un numar: "))
            print(get_largest_prime_below(numar))
        elif optiune == "2":
            nr=input("introduceti nr: ")
            if is_palindrome(nr):
                print("Numarul dat este palindrom.")
            else:
                print("Numarul dat nu este palindrom.")






if __name__ == '__main__':
    main()