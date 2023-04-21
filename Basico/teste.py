import secrets

length = 50
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

secret_key = ''.join(secrets.choice(chars) for i in range(length))

print(secret_key)
