

def main():
    s = ''
    s = input()
    print(isPalindrome(s))

def isPalindrome(s):
    if(len(s)<2):
        return True
    if(s[0]!=s[-1]):
        return False
    return isPalindrome(s[1:-1])



if __name__ == '__main__':
    main()
