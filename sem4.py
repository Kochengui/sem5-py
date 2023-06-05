# 1).

def num(a,b): 
   
   if b==0:
     
      return 1
  
   return num(a,b-1)*a
a=int(input('введите число: '))
b=int(input('введите степень: '))

print(num(a,b))


# 2).
def ten_to_two(n):
    if n == 0 or n == 1:
        return f'{n}'
    return ten_to_two(n // 2) + f'{n % 2}'


n = int(input('введите число : '))
print(ten_to_two(n))