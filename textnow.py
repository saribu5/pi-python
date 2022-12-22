import pytextnow
#for documentation, look here:
#https://github.com/leogomezz4t/PyTextNow_API

print("client: saribu123456789" + "\n" + "default number: 7739461290" + "\n" + "type RESET to reset connection")

client = pytextnow.Client("saribu123456789", sid_cookie="s%3AUzsByyP17-jUQw9p9OkT9aUO0p0dMf30.2fo2H6mslDXuJsDl77W22z2uhIn2oMfFqvvUA4Ngzo4", csrf_cookie="s%3AUekUtN0a6_yCVeFrQav2Ncp7.SjKCj8OLLfiiYBMw9w9Ne%2B%2BilGSdcZibukdBVrnSxUo")

num = input("number: ")
if (num == ""):
	num = "7739461290"

print("options: " + "\n" + "1: send normal message" + "\n" + "2: send mms message (image)" + "\n" + "3: get all messages" + "\n" + "4: get all sent messages" + "\n" + "5: RESET" + "\n")
opt = input()

if (opt == "1"):
	msg = input("message: ")
	client.send_sms(num, msg)
elif (opt == "2"):
	file = input("input file: ")
	client.send_mms(num, file)
elif (opt == "3"):
	messages = client.get_messages
	print(messages)
elif (opt == "4"):
	sentmsgs = client.get_sent_messages
	print(sentmsgs)
elif (opt == "5"):
	client.auth_reset()

print("operation complete")
