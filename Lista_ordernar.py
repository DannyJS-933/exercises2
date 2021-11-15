import random
#Ordene la siguiente lista en forma ascendente
list_1 = [10, 5, 7, -1, 33, 25, 66, 3, 3]
print(f'Lista original: {list_1} ')
list_1.sort()
print(f'Lista ordenada de forma ascendente: {list_1}')
#--------------------------------------------------------------------------------
#Intercambie los valores de la posición 0 y 1 de la siguiente lista. 
list_2 = ['A', 'B']
print(f'Lista original: {list_2}')
list_2.sort(reverse=True)
print(f'Nueva lista: {list_2}')
#--------------------------------------------------------------------------------
#Cree una lista de los primeros 25 valores de la serie de Fibonacci
fibonacci_list = [0,1]
for i in range(0,26):
    fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i + 1])
print(fibonacci_list)
#--------------------------------------------------------------------------------
#Genere una lista de 30 número aleatorios
random_list = []
for i in range(0,30):
    random_number = random.randint(0,30)
    random_list.append(random_number)
print(random_list)
#------------------------------------------------------------------------------------------------------
# #Genere una lista de 20 números aleatorios sin que hayan repetidos y que se encuentren
# entre 0 (cero) y 23
random_list2 = []
for i in range(1):
    random_number2 = random.sample(range(23), 20)
    random_list2.append(random_number2)
print(random_list2)
