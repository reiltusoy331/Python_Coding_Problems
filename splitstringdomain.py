# extract the "umbrellacorp.com" domain in email address researchteam@umbrellacorp.com 

email = "researchteam@umbrellacorp.com"
mailbox = email.split('@')[0]
domain = email.split('@')[1]

print(domain)
print(mailbox)
