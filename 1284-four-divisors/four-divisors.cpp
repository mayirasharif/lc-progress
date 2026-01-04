class Solution {
public:

#include <cmath>

    bool hasFourDivisors(int num) {
                // 1 -> sqrt(num) for comparison
                
                float root = sqrt(num);
                int count = 0;
                for (int z = 1; z * z <= num; z++) {
                    if (num % z == 0) {
                        if (z * z == num) {
                            count += 1;
                        } else {
                            count += 2;
                        }
                    }
                    if (count > 4) return false;
                }
                return count == 4;
            }

    int addDivisors(int num) {
            float root = sqrt(num);
            int summs = 0;

            for (int z = 1; z <= root; z++) {
                if (num % z == 0) {
                    summs += z;

                    if (z * z != num) {
                        summs += (num / z);
                    }

                    }
                }
            return summs;

        }

    int sumFourDivisors(vector<int>& nums) {

        // hmm.. return the sum of divisors of the integers in array
        // that have exactly four divisors

        int sum = 0;
        for (int i: nums) {

            // find the divisors and sum them
            if (hasFourDivisors(i)) {
                sum += addDivisors(i);
            }

            

        }

        return sum;
        
    }
};