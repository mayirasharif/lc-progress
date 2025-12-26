class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        

        h = sorted(happiness)[::-1]

        decr = 0

        result = 0
        i = 0
        while k > 0:
            print(result)
            if decr > h[i]:
                pass
            else:
                result += h[i] - decr
            print(result)
            decr += 1
            k -= 1
            i += 1
        return result


        