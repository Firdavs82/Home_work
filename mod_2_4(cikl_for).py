numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
for i in range(len(numbers)+1):
    if i <= 1:
        i += 1
        continue
    is_prime = 0
    for j in range(1,len(numbers)):
        if i % j == 0:
            is_prime += 1
    if is_prime == 2:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)