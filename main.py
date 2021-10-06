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
        
        
def get_age_in_days(birthday):
    '''
    Determina varsta unei persoane in zile.
    :param birthday: numere intregi
    :return: returneaza varsta unei persoane, in zile.
    '''
    today=date.today()      
      birthday= today - birthday_date

 def birthday_date(datan : str) :
     '''
     Functia converteste sirul in datetime.
     
     '''
         
         
         
       
