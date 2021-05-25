# youtube-api
youtube-apiを叩いてみる

1. こちらのサイトへアクセスする。(https://github.com/kuroroblog/youtube-api/tree/master)
2. 緑の「Code」と書かれたボタンをクリックする。
3. 「Download ZIP」ボタンをクリックする。
4. ダウンロードしたzipファイルをデスクトップへ移動する。
5. zipファイルをダブルクリックして展開する。
6. ターミナルを開く。
7. youtube-api-master ディレクトリへ移動する。(`cd`コマンドを利用する。)
8. こちらのサイトから事前にyoutubeのAPI鍵を取得する。(https://qiita.com/g-k/items/7c98efe21257afac70e9#youtube-data-api%E3%81%AE%E7%99%BB%E9%8C%B2)
9. youtube-api-master ディレクトリにて`echo "YOUTUBE_API_KEY=AIzaから始まるyoutubeのAPI鍵" > .env`を実行する。(AIzaから始まるyoutubeのAPI鍵の文字列を8で取得したyoutubeのAPI鍵へ変更ください。)
10. youtube-api-master ディレクトリにて`pip install -r requirements.txt`を実行する。
11. `python main.py`を実行する。
