n = 10000   

def fibonacci_gen(n) -> int:
    yield 0
    prev2 = 0
    prev1 = 1
    while prev1 <= n:
        result = prev1+prev2
        prev2 = prev1
        prev1 = result
        yield result

for i in fibonacci_gen(n) :
    print(i)
    