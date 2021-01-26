def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(a,b,c):
    if a==b:
        d=word[len(c):0:-1]
        if c==d:
            return True
        else:
            return False
    else:
        return False
word=input("Enter a string:").lower()
a=first(word)
b=last(word)
c=middle(word)
p=is_palindrome(a,b,c)
print(p)
        
