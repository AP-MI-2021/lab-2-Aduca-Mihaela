def print_menu():
    print("1. Verifica daca un numar este prim.")
    print("2. Verifica daca un numar este palindrom.")
    print("3. Verifica daca un numar este superprim.")
    print("4. Iesire.")


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
    aux = n
    while aux != 0:
        cifra = aux % 10
        ogl = ogl * 10 + cifra
        aux = aux // 10
    if ogl == n:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(131) == True
    assert is_palindrome(222) == True
    assert is_palindrome(214) == False

def is_superprime(n):
    '''
    Determina daca un numar este superprim sau nu.
    :param n:
    :return: true daca numarul este supraprim si False in caz contrar.
    '''
    copie = n
    verificare = 1
    while copie:
        if not is_prime(copie):
            verificare = 0
            break
        copie=copie // 10
    if verificare == 1:
        return True
    return False


def test_is_superprime():
    assert is_superprime(124) == False
    assert is_superprime(1290) == False
    assert is_superprime(239) == True
    assert is_superprime(14) == False

def main():
    test_get_largest_prime_below()
    test_is_palindrome()
    test_is_superprime()

    while True:
        print_menu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            numar=int(input("Dati un numar: "))
            print(get_largest_prime_below(numar))
        elif optiune == "2":
            nr=int(input("introduceti nr: "))
            if is_palindrome(nr):
                print("Numarul dat este palindrom.")
            else:
                print("Numarul dat nu este palindrom.")
        elif optiune == "3":
            nr1 = int(input("dati un nr: "))
            if is_superprime(nr1):
                print("Numarul dat este superprim.")
            else:
                print("Numarul dat nu este superprim.")
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Reincercati: ")






if __name__ == '__main__':
    main()