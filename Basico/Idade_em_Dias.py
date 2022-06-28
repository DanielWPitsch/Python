
dias = int(input())
anos = dias/365
meses = int((dias-(int(anos)*365))/30)
dias = (dias-(int(anos)*365))%30

print(str(int(anos))+' ano(s)')
print(str(int(meses))+' mes(es)')
print(str(dias)+' dia(s)')  