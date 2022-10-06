from random import randint

P = int(input("Enter a value of P: "))
G = randint(0, P-1)

print("The Value of P is: ", P)
print("The Value of G is: ", G)

a = int(input("Enter the value of a: "))
print("The Private Key a for Alice is: ", a)
x = int(pow(G,a,P))

b = int(input("Enter the value of b: "))
print('The Private Key b for Bob is : ', b)
y = int(pow(G,b,P))

ka = int(pow(y,a,P))
kb = int(pow(x,b,P))
print('Secret key for the Alice is : ', ka)
print('Secret Key for the Bob is : ', kb)