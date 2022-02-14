N = int(input())
every_button = 2**N - 1
even_button = int('10'*(N//2), 2)
odd_button = int('10'*((N-1)//2)+'1', 2)

print(every_button)
print(even_button)
