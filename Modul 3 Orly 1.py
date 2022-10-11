numbers = [5,32,56,2,2,16,7,10,23,100,18]
print(numbers)
mean_number = 0

for i,n in enumerate(numbers):
    bezreszty = n//10
    zreszta = 10 if n%10 >= 5 else 0
    numbers[i] = bezreszty * 10 + zreszta

print()
print(numbers)
numbers.remove(max(numbers))
numbers.remove(min(numbers))
print(numbers)
print()
mean_number = sum(numbers) / len(numbers)
print(mean_number)


"""

for i,n in enumerate(numbers):
  print(i,n)
  tens = n//10
  remainder = 10 if n%10 >= 5 else 0
  numbers[i] = tens*10 + remainder

print(numbers)

"""
