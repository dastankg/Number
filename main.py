from cryptography.fernet import Fernet

str1 = "996777112233"
str2 = "996777112232"
str3 = "996777112231"
key = b'9cVYDlqshER_Rg2zLQR_huBPKAilATrncGiFnSzkBns='


fernet = Fernet(key)

enctex = fernet.encrypt(str1.encode())
enctex1 = fernet.encrypt(str2.encode())
enctex2 = fernet.encrypt(str3.encode())

dectex = fernet.decrypt(enctex).decode()


print(enctex)
print(enctex1)
print(enctex2)
# with open('static/code.txt', 'rb') as f:
#     file = f.read()
#     print(fernet.decrypt(file).decode())