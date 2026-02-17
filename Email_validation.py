# Email Validation in Python using Regular Expression

import re

# Make a regular expression for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Define a function for validating Email
def check(email):
    if re.fullmatch(regex, email):
        print("Valid Email")
    else:
        print("Invalid Email")

# Driver Code
if __name__ == '__main__':
    check("ankitrai326@gmail.com")
    check("my.ownsite@our-earth.org")
    check("ankitrai326.com")


#---------------check URL---------------
    import re

def isValidURL(url):
    regex = r"((http|https)://)(www.)?[a-zA-Z0-9@:%._\+~#?&//=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%._\+~#?&//=]*)"
    
    if re.fullmatch(regex, url):
        return True
    else:
        return False

# Driver Code
if __name__ == "__main__":
    url = "http://atestc.edu.in/"
    
    if isValidURL(url):
        print("Valid URL")
    else:
        print("Invalid URL")
