def count_upto(n):
      ns = []
      while n>=0:
            ns,n = [n]+ns,n-1
      return ns


print(count_upto(0)) # [0]
print(count_upto(5)) # [0, 1, 2, 3, 4, 5]
print(count_upto(-3)) # []
