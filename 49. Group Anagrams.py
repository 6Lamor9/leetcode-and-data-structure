# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(strs):
    d = {}
    for word in strs:
        key = tuple(sorted(word))
        d[key] = d.get(key, []) + [word]
    return d.values()
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

