password = '1234'
i = 3
while i > 0:
	i = i - 1
	word = input('請輸入密碼: ')
	if word == password:
		print('密碼正確，登入中')
		break
	else:
		print('密碼錯誤')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('帳號鎖定')
