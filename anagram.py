'''
Input : s1 = "listen"
        s2 = "silent"
Output : The strings are anagrams.


Input : s1 = "dad"
        s2 = "bad"
Output : The strings aren't anagrams
'''


str1=input("enter 1st string:")
str2=input("enter 2nd string:")

print(str1,sorted(str1))
print(str2,sorted(str2))

if sorted(str1)==sorted(str2):
    print("anagram")
else:
    print("not anagram")