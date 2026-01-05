#include <sstream>
#include <string>
#include <iostream>

class Solution {
public:
    int lengthOfLastWord(string s) {

        // parsing
        std::stringstream myStream(s);

        int stringLength;
        std::string word;

        while (myStream >> word) {
            stringLength = word.size();
        }

        return stringLength;


        // examine length of last index
        
    }
};