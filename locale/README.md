## このフォルダについて
うみてるが制作した、Freecivの翻訳パッチです。  
最新版の翻訳を参考に、現在の安定版で未翻訳の部分をうみてるが翻訳しました。

## 導入方法
### 1. 翻訳ファイルのダウンロード
ダウンロードURL:  
[https://github.com/umiteru2004/freeciv/raw/develop/locale/LC_MESSAGES/freeciv-core.mo](https://github.com/umiteru2004/freeciv/raw/develop/locale/LC_MESSAGES/freeciv-core.mo)
### 2. 翻訳ファイルの場所を開く
デフォルトの翻訳ファイルは、
```
Freecivのプログラムフォルダ/share/locale/ja/LC_MESSAGES/freeciv-core.mo
```
です。  
プログラムフォルダの場所は環境によって異なります。  
最新のHomebrewでFreeciv v3.1.2をインストールした場合、プログラムフォルダは
```
/opt/homebrew/Cellar/freeciv/3.1.2
```
です。
### 3. 翻訳ファイルの置き換え
デフォルトの`freeciv-core.mo`をダウンロードしたものに置き換えます。  
万が一置き換えによって不具合が発生した際に、簡単に復元できるように、  
デフォルトの`freeciv-core.mo`はプログラムフォルダの外の別の場所に取っておくと良いと思います。
### 4. 完了
Freecivを起動して、翻訳が適用されていることを確認してください。
