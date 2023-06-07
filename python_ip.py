import requests

ip_user = str(input("Enter ip "))
print("\r")
send_request = requests.get(f"https://api.iplocation.net/?ip={ip_user}")
b = send_request.json()
# 8.8.8.8
for i in b:
	print(i," : ",b[i])