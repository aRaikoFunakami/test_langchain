# test_langchain
langchainライブラリを使ってchatgptとチャットする非常にシンプルなプログラム

# 利用方法
1. app.pyを起動する
2. ウェブブラウザでtpp.pyにアクセスする
3. ChatGPTに送りたい文字列を `?text=<chatgptに送りたい文字列>` で指定する
3. ChatGPTからの回答はブラウザに表示される

## test_langchainを起動
ターミナルで app.py を実行する
```
poetry install
poetry run python app.py
```

## 次のようなURL指定してウェブブラウザでアクセスする
- http://localhost:8080/?text=what%20is%20your%20name
- http://localhost:8080/?text=how%20are%20you
- http://localhost:8080/?text=what%20is%20mt.Fuji
- http://localhost:8080/?text=who%20is%20the%20fastest%20man