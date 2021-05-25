# 参考 : https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9#python-dotenv%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8env%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E4%BD%9C%E6%88%90
import os
from os.path import join, dirname
# 参考 : https://qiita.com/g-k/items/7c98efe21257afac70e9#python%E3%81%A7api%E3%81%8B%E3%82%89%E6%83%85%E5%A0%B1%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AE%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%82%92%E5%8F%96%E5%BE%97
from apiclient.discovery import build
# 参考 : https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9#python-dotenv%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8env%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E4%BD%9C%E6%88%90
from dotenv import load_dotenv

# .envファイルのパスを取得する。
dotenvPath = join(dirname(__file__), '.env')
# .envファイルを読み込む。
load_dotenv(dotenvPath)

# .envファイルに書き込まれる鍵情報を取得する。
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# 以下参考
# https://qiita.com/g-k/items/7c98efe21257afac70e9#%E7%89%B9%E5%AE%9A%E3%82%AD%E3%83%BC%E3%83%AF%E3%83%BC%E3%83%89%E3%82%92%E5%90%AB%E3%82%80%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB%E3%81%AE%E5%8B%95%E7%94%BB%E3%82%92%E5%86%8D%E7%94%9F%E5%9B%9E%E6%95%B0%E9%A0%86%E3%81%A7%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',
    q='手芸',
    type='video',
).execute()

for item in search_response['items']:
    print(item['snippet']['title'])
