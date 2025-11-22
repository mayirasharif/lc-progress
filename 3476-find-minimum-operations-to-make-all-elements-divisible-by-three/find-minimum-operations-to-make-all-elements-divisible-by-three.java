class Solution {
    public int minimumOperations(int[] nums) {
        Integer operations = new Integer(0);
        for (int num : nums) {
            if (num % 3 == 0) {
                continue;
            }
            operations++;

        }
        return operations;

    }
}