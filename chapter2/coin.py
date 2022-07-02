print("how many money would you like to take out:", end="")
num=int(input())
hundreds=(num//100)
fifty=(num%100)//50
tens=(num%50)//10
print("hundreds %d" %hundreds)
print("fifty %d" %fifty)
print("tens %d" %tens)

