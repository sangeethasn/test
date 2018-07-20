
# Python program to check validation of password
# Module of regular expression is used with search()
import re
password = raw_input("Enter the password 'R@m@_f0rtu9e$' ")
while True:
    if (len(password)<6):
        print('Invalid password-length is too small')
        break

    elif (len(password)>12):
        print('Invalid password-length is too big')
        break

    elif not re.search("[a-z]", password):
        print('Invalid password-Should have atleast one character between a-z')
        break

    elif not re.search("[A-Z]", password):
        print('Invalid password-Should have atleast one character between A-Z')
        break

    elif not re.search("[0-9]", password):
        print('Invalid password-Should have atleast one character between 0-9')
        break

    elif not re.search("[#@$]", password):
        print('Invalid password-Should have atleast one special character from the list [$,#,@]')
        break

    else:
        print("Valid Password")
        break

