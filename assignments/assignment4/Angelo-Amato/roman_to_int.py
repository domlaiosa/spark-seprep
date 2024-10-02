#Solution to LeetCode's "Roman To Integer" Problem: Found at: https://leetcode.com/problems/roman-to-integer/

def romanToInt(s: str) -> int:
    #dictionary with roman numeral's values in arabic numerals
    letters = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    num = 0
    for i in range(len(s)):
        #checks the numeral after the current one, if it is less it should subtract the indexed value from the running sum
        if (i+1 != len(s)) and (letters[s[i]] < letters[s[i + 1]]):
            num -= letters[s[i]]
        #if not add the indexed value to the running sum
        else:
            num += letters[s[i]]
    return num

#test cases
assert romanToInt("III") == 3
assert romanToInt("IV") == 4
assert romanToInt("IX") == 9
assert romanToInt("LVIII") == 58
assert romanToInt("XCIV") == 94
assert romanToInt("MCMXCIV") == 1994
assert romanToInt("MMXXIV") == 2024