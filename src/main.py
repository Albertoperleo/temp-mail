import requests as req
import time

api_url = 'https://www.1secmail.com/api/v1/'
gen_mail = '?action=genRandomMailbox&count=1'

new_mail = req.get(api_url+gen_mail).json()
print(new_mail[0]) #returns an array

#parsing the mail to build the mailbox req
parse = new_mail.split('@')
'''
name = parse[0]
dom = parse[1]
print(name, dom)
'''


#check_mailbox = '?action=getMessages&login='+ +'&domain='+
