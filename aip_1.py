import requests
import pprint
import json

a = input('食べたいものは？')
b = input('場所は？')

#レストラン検索APIのURL
url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

#パラメータの設定
params={}
params["keyid"] = "a99713ebf66daad045df9e9eb605b893" #取得したアクセスキー
params["freeword"] = (a + ',' + b)
#リクエスト結果
result_api = requests.get(url, params)
result_api = result_api.json() # 読まなきゃいけない！じゃないと<Response [200]>とでるだけ。
# print(result_api) # 整形せずにそのまま表示
# pprint.pprint(result_api) # 整形して表示

hit = len(result_api['rest'])
print(hit)
# 10 #目黒エリアでフリーワード「すし」は10コある！

# ループで、ヒットした10件分の店名を表示させる
for i in range(hit):
    print(result_api['rest'][i]["name"])
    print(result_api['rest'][i]['address'])
    print()
