class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # given: candidates list, target integer
        # return: unique combos of candidates -> sum to target

        # combinations? -> backtracking

        res = [] # append all viable combos here
        n = len(candidates)
        def findSum(i, combo=[]):
        # backtracking solution -> basic algo
        # 2 choices per i (index):
        #  select the element
        #  NOT select the element
            if sum(combo) > target:
                return

            if i > n-1:
                if sum(combo) == target:
                    if combo not in res:
                        res.append(combo)
                    
                return
            # check if curr combo is legit
            if sum(combo) == target:
                if combo not in res:
                    res.append(combo)

            # instance where we select curr val
            findSum(i+1, combo)
            findSum(i+1, combo + [candidates[i]])
            findSum(i, combo + [candidates[i]])
        
        findSum(0)
        return res











