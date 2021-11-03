# Domain

email = input('Enter email: ')
if email.find('@', 1, -3) != -1:
    list_email = email.split('@')
    if list_email[-1] == 'gmail.com':
        print(email)
    else:
        print('DOMAIN NAME is not supported')
else:
    print('wrong enter email')
