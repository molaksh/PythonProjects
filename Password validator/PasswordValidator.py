import re


def validate(str):
    splchr = ['$','#','@']
    if (len(str) < 6 or len(str) > 12) or (
        re.search('[0-9]',str) is None) or (
            re.search('[A-Z]',str) is None) or (
                re.search('[a-z]',str) is None) or (
                    not any(char in splchr for char in str)
                ):
        print("not valid")
    else:
        print("valid")
            

def main():
    
    user_input = input('> ')
    while  user_input != 'quit':
        validate(user_input)
        user_input = input('> ')


main()