# Google foobar challenge
def is_prime(n, previous_primes):
    for prime in previous_primes:
        if n%prime == 0:
            return False
    return True

# Output first i+5 prime numbers
def construct_prime_string(i):
    base = [2,3,5,7,11]
    needed = i+5-len(base)
    current = base[-1]+1
    while needed>0:
        if is_prime(current,base):
            base.append(current)
            needed -= 1
        else:
            current+= 1
    
    return "".join(list(map(lambda num: str(num), base)))

def solution(i):
    return construct_prime_string(i)[i:i+5]

print(solution(10000))