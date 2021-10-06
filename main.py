'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
 # codul vostru aici
  if (n==0 or n==1):
    return False
  for d in range (2, n//2):
    if (n%d==0):
      return False
  return True
  pass
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  prod = 1
  for el in range(0, len(lst)):
    prod = prod * lst[el]
  return prod
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
    while (x!=y):
    if (x>y): x = x - y
    else : y = y - x
  print ("cmmdc",x)
  return x
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  
def main():
  # interfata de tip consola aici
print( '''
 1. IS prime
 2. Product
 3. Cmmdc v1
 4. Cmmdc v2
 ''')
  a= int (input("Comanda:"))
  if (a==1):
    # is prime
    n= int (input ("Introduce n="))
    print (is_prime(n))
  if(a==2):
    # product
    n=int (input ("Introduce n="))
    list=[]
    for i in range(0, n):
      el= int (input())
      list.append(el)
    #print (list)
    #print(len(list)) #lungimea
    print("produs=" ,gen_product(list))
  if (a==3):
    # cmmdc v1
    x= int (input ("Introduce x="))
    y= int (input ("Introduce y="))
    print(get_cmmdc_v1(x, y))
    
if __name__ == '__main__':
  main()
