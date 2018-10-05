'''Solution to:
    https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
    function finds the number of anagrams contained in a certain string'''

def substrings(word):
    strings=[]
    for l in range(1,len(word)):
        sub = [word[i:i+l] for i in range(len(word)-l+1)]
        strings.append(sub)
    return strings

def anagrams(word):
    count = 0
    #create a list of all possible words at each length
    words = substrings(word)
    for i in range(len(words)):
        for j in range(len(words[i])):
            gram = sorted(words[i][j])
            for k in range(j+1,len(words[i])):
                if gram == sorted(words[i][k]):
                    count+=1
    return count

word = 'kkkk'

anagrams(word)
