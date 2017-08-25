import requests

r = requests.get('http://book.impress.co.jp/ --proxy=http://e024779:tiyoyo7!@172.17.96.21:12080')

print(r.status_code)