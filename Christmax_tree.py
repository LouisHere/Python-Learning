num = int(input("number:"))
i = 1 
for i in range(1,num+1):
  space = num - i
  star = 2 * i - 1
  print(" "*space+"*"*star)

s = 1
d = num//2 + 2
for s in range(1,d):
   space2 = num - 1
   print(" "*space2+"+")

input("Prease <enter>")