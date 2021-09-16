import requests
import numpy as np

users_pass = {"user1": "pass1", "user2": "pass2"}

user = input()
cur = int(input())
set = int(input())
crypto = input()

sell = [
    {"user1":
         [
             {
                 "btc":[[100, 200], [300, 600]]
             },
             {
                 "eth": [[500, 700]]
             }
          ]
    }
]

buy = [
    {"user1":
         [
             {
                 "btc": [[700, 500]]
             },
             {
                 "eth": [[432, 123]]
             }
         ]
    }
]

if user not in list(users_pass.keys()):
    if cur == set:
        print("send email")

    if cur < set:
        sell.append({user:[{crypto:[[cur, set]]}]})
        users_pass[user] = "deafault"

    if cur > set:
        buy.append({user:[{crypto:[[cur, set]]}]})
        users_pass[user] = "deafault"

else:
    if cur == set:
        print("Sending email")
    if cur < set:
        flag = 0
        for users in sell:
            for key_user in users:
                if key_user == user:
                    # print("found ",user)
                    # print(users[key_user])
                    for dict_of_cryptos in users[key_user]:
                        for key_crypto in dict_of_cryptos:
                            temp = []
                            if crypto in list(dict_of_cryptos.keys()):
                                dict_of_cryptos[crypto].append([cur, set])
                                # temp.append([cur, set])
                            else:
                                # dict_of_cryptos[crypto] = [cur, set]
                                users[key_user].append({crypto: [[cur, set]]})
                                flag = 1
                                break
                        if flag == 1:
                            break


    if cur > set:
        flag = 0
        for users in buy:
            for key_user in users:
                if key_user == user:
                    # print("found ",user)
                    # print(users[key_user])
                    for dict_of_cryptos in users[key_user]:
                        for key_crypto in dict_of_cryptos:
                            if crypto in list(dict_of_cryptos.keys()):
                                # dict_of_cryptos[crypto].append([cur, set])
                                break
                            else:
                                # dict_of_cryptos[crypto] = [cur, set]
                                users[key_user].append({crypto:[[cur, set]]})
                                flag=1
                                break
                        if flag == 1:
                            break

print(sell)
print(buy)
response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false").json()
currency = np.array(response)

# print(len(currency))
for x in currency:
    # print(x['id'],"-->",x['current_price'])
    pass