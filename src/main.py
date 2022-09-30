import requests as req
import time

api_url = 'https://www.1secmail.com/api/v1/'
gen_mail = '?action=genRandomMailbox&count=1'

genMail = req.request("GET", api_url + gen_mail).json()
print('Operative mail: ' + genMail[0]) #returns an array

#parsing the mail to build the mailbox req or readMail req
mail = genMail[0].split('@')
getMailbox = '?action=getMessages&login='+mail[0]+'&domain='+mail[1]
getMail = '?action=readMessage&login=' + mail[0] + '&domain=' + mail[1] + '&id='

#check mail-box
last_mail = None
while(True):
    time.sleep(5)
    mailbox = req.request("GET", api_url + getMailbox).json()
    if len(mailbox) > 0 and last_mail != mailbox[0]:
        print(mailbox[0])
        last_mail = mailbox[0]
        getById = getMail + str(last_mail["id"])
        res = req.request("GET", api_url + getById).json()
        readMail = res["textBody"]

        for line in readMail.split('\n'):
            print(line)