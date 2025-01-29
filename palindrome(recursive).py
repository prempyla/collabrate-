def is_palindrome(s):
    if len(s)<=0:
        return True

    if s[0]!=s[-1]:
        return False

    if is_palindrome(s[1:-1]):
        return True
