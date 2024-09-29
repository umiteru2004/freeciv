## このフォルダについて
うみてるが制作した、Freecivの翻訳パッチです。  
最新版の翻訳を参考に、現在の安定版で未翻訳の部分をうみてるが翻訳しました。

## 導入方法
### 1. 翻訳ファイルのダウンロード
2つの翻訳ファイルをダウンロードします。  
ダウンロードURL:  
- [https://github.com/umiteru2004/freeciv/raw/develop/locale/freeciv-core.mo](https://github.com/umiteru2004/freeciv/raw/develop/locale/freeciv-core.mo)
- [https://github.com/umiteru2004/freeciv/raw/develop/locale/freeciv-nations.mo](https://github.com/umiteru2004/freeciv/raw/develop/locale/freeciv-nations.mo)
### 2. デフォルトの翻訳ファイルを探す
デフォルトの翻訳ファイルは次のフォルダにあります。  
ファイル名は、ダウンロードしたものと同じ`freeciv-core.mo`および`freeciv-nations.mo`です。
```
Freecivのプログラムフォルダ/share/locale/ja/LC_MESSAGES/
```
プログラムフォルダの場所は環境によって異なります。  
例えば、最新のHomebrewでFreeciv v3.1.2をインストールした場合、プログラムフォルダは以下の通りです。
```
/opt/homebrew/Cellar/freeciv/3.1.2/
```
また、[公式サイトのダウンロードページ](https://freeciv.org/download.html)に掲載されているWindowsパッケージをインストールした場合、  
プログラムフォルダは、デフォルトで`C:¥Program Files¥`に格納されています。
```
C:¥Program Files¥Freeciv-3.1.2-win64-10-client-gtk3.22
```
### 3. 翻訳ファイルの置き換え
デフォルトの`freeciv-core.mo`および`freeciv-nations.mo`をダウンロードしたものに置き換えます。  
問題が発生した際に元に戻せるように、デフォルトのファイルは、  
プログラムフォルダの外の別の場所に取っておくと良いと思います。
### 4. 完了
Freecivを起動して、翻訳が適用されていることを確認してください。
