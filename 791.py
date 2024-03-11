from collections import defaultdict, Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        str_dict = Counter(s)

        new_str =""
        for letter in order:
            new_str += letter*str_dict[letter]
            del str_dict[letter]

        for key in str_dict.keys():
            new_str += key*str_dict[key]

        return new_str
