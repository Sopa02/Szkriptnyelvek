from operator import truediv


def isPalindrome(s):
    if(s == s[::-1]):
        return True
    return False



def main():
    s = ''
    s = input()
    print(isPalindrome(s))




if __name__ == '__main__':
    main()