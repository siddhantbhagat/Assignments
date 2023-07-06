def First_unique_char(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            return i

print(First_unique_char('leetlcode'))




