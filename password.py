password = '1234'
i = 3
while i > 0:
	word = input('請輸入密碼: ')
	if word == password:
		print('密碼正確，登入中')
		break
	else:
		i = i - 1
		print('密碼錯誤，還有', i, '次機會')
print('密碼鎖定')