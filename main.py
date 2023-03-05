lims = input("Enter your sigma boundaries in order from start:finish seperated by \":\": ")
equ = input("Enter your equation & your index as \"j\": ")
a, down, up, count, mul, add, div, sub, f = 0, 0, 0, 0, 0, 0, 0, 0, 0
for i in range(len(lims)):
   if lims[i] == ":":
      a = i
down, up = int(lims[0:a]), int(lims[a+1:len(lims)])
for k in range(len(equ)):
   # mults
   if equ[k] == "j":
      mul = int(equ[k-1])
   if equ[k] == "*":
      if equ[k-1].isdigit():
         mul = mul * int(equ[k+1])
      else: mul = mul * int(equ[k-1])
   # minus
   # add
# main process
for x in range(down, up + 1, 1):
   count = count + (x * mul)
print(count)
