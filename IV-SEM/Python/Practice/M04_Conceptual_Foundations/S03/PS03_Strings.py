'''
1. Reverse a string
2. Palindrome or not
3. Anagram
'''
# s = "Python"
# s = s.replace('y','i')
# print(s)
# s = "nandu"
# print(s.capitalize())
# print(s)

# def reverse_str(s):
#     res = ""
#     for i in s:
#         res = i+res
#     return res
# print(reverse_str("abc"))
# print(reverse_str("python"))

# def reverse_str(s):
#     return s[::-1]
# print(reverse_str("python"))

# def reverse_str(s):
#     res = ""
#     stop = -1*(len(s)+1)
#     for i in range(-1,stop,-1):
#         res = res + s[i]
#     return res
# print(reverse_str("abc"))

# def is_palindrome(s):
#     res = ""
#     for i in s:
#         res = i + res
#         if res == s:
#             return True
#     return False
# print(is_palindrome("nandu"))
# print(is_palindrome("madam"))

# def Frequency_count(s):
#     freq = {}
#     for ch in s:
#         # freq[ch] = freq.get(ch,0) + 1
#         if ch not in freq:
#             freq[ch] = 1
#         else:
#             freq[ch] += 1
#     return freq

# print(Frequency_count("abcabc"))

# def Anagram(s1,s2):
#     return Frequency_count(s1) == Frequency_count(s2)
# print(Anagram("abcabc","aabbcc"))

from collections import Counter
print(Counter("aabbcc"))