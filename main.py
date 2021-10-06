from datetime import date

def is_prime(n):
    """
    Verifica daca un numar este prim sau nu.
    :param n:numar natural
    :return:Returneaza True daca un numar este prim si False in caz contrar.
    """

    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, x//2 + 1):
        if n % i == 0:
            return False
   return True

    def get_largest_prime_below(n):
     """
     Gaseste cel mai mare numar prim, mai mic decat parametrul n.
     :param n:numar natural.
     :return:Returneaza cel mai mare numar prim, mai mic decat parametrul n, sau False in cazul in care nu exista un astfel de numar.

     """
     while n - 1 > 0:
         if is_prime(n - 1):
             return n - 1
         n = n - 1
     return False



     def test_get_largest_prime_below():
         """
         Verifica daca functia functioneaza.
         :return:numar natural
         """
         assert get_largest_prime_below(4) == 3
         assert get_largest_prime_below(7) == 5
         assert get_largest_prime_below(2) is False.
        
        

  def is_palindrome(n)
    '''
        Verifica daca un numar dat este palindrom sau nu.
    :param n: intreg
    :return: Returneaza True daca numarul n este palindrom, sau va returna False in caz contrar.
    '''
        x=n
        ogl=0
         while x:
             ogl=ogl*10+x%10
             x=x//10

        if ogl == n:
            return True
    return False


def test_is_palindrome():
    assert is_palindrome(3223) is True
    assert is_palindrome(6453) is False
    assert is_palindrome(898) is True
    assert is_palindrome(212) is True

test_is_palindrome()

def main():
    while True:
        print("1.Determina daca un numar dat este palindrom.")

        optiune = input("Dati optiunea:")
        if optiune == "1":
            numar = int(input("Dati numar:"))
            if is_palindrome(numar):
                print("Numarul dat este palindrom.")
            else:
                print("Numarul dat nu este palindrom.")

         
    if __name__ == '__main__':
        main()      
        
         
         
         
       
