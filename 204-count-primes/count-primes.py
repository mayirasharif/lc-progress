class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False


        # True algorithm (Sieve)

        p = 2 # start at 2 due to it being first prime number
        
        # loop until:
        while p * p < n:
            if isPrime[p]:
                # elim multiples

                for i in range(p * p, n, p):
                    isPrime[i] = False
            p += 1
        
        # collect
        res = 0
        for j in isPrime:
            if j:
                res += 1
        return res

        
















        
        p = 2
        while p * p < n:
            if isPrime[p]:
                for i in range(p * p, n, p):
                    isPrime[i] = False
            p += 1
        
        return sum(isPrime)