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

![image](https://github.com/aRaikoFunakami/test_langchain/assets/611793/c0260b75-323c-46a3-b397-7f1295600b58)

- http://localhost:8080/?text=how%20are%20you

![image](https://github.com/aRaikoFunakami/test_langchain/assets/611793/24ea5868-2c42-43db-b245-f5ecb7b9b593)

- http://localhost:8080/?text=what%20is%20mt.Fuji

![image](https://github.com/aRaikoFunakami/test_langchain/assets/611793/4a044a96-c704-409e-a061-2007e848d486)

- http://localhost:8080/?text=who%20is%20the%20fastest%20man

![image](https://github.com/aRaikoFunakami/test_langchain/assets/611793/b1693c2f-482b-4077-b46f-39617ff38875)
