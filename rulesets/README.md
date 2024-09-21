# ルールセットの導入方法
## 1. ダウンロード
うみてるのFreecivフォルダのZipをダウンロードします。  
このフォルダには、ルールセット以外のファイルも含まれています。  
  
ダウンロードURL:  
[https://github.com/umiteru2004/freeciv/archive/refs/heads/develop.zip](https://github.com/umiteru2004/freeciv/archive/refs/heads/develop.zip)
## 2. ルールセットのフォルダを取り出す
ルールセットのフォルダは、前項でダウンロードしたZipを解凍してできる`freeciv-develop`フォルダの中の、`rulesets`フォルダの中にあります。  
  
導入するルールセットのフォルダと、それに対応する`.serv`ファイルを、デスクトップなどの適当な場所に取り出してください。  
例えば、Civ2-3MP2Umiルールセットを導入する場合は、以下のフォルダとファイルを取り出します。
```
freeciv-develop/rulesets/civ2-3mp2umi/
freeciv-develop/rulesets/civ2-3mp2umi.serv
```
## 3. .freecivフォルダを探す
`.freeciv`フォルダを探します。  
デフォルトでは、Freecivがインストールされているコンピュータの、ユーザーフォルダの中にあります。  
ユーザーフォルダは、Macの場合`/Users`に、Windows 11の場合`C:¥Users`に、Linuxの場合`/home`にあります。
  
ただし、`.freeciv`は隠しフォルダです。  
隠しフォルダを表示する方法は以下の通りです。  
  
Macの場合:  
Finderを開いて、ショートカットキー「⌘ command」+「⇧ shift」+「.」です。  
  
Windowsの場合:  
以下のWebサイトを参照してください。  
[https://support.microsoft.com/ja-jp/windows/windows-の隠しファイルと隠しフォルダを表示する-97fbc472-c603-9d90-91d0-1166d1d9f4b5](https://support.microsoft.com/ja-jp/windows/windows-%E3%81%AE%E9%9A%A0%E3%81%97%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%A8%E9%9A%A0%E3%81%97%E3%83%95%E3%82%A9%E3%83%AB%E3%83%80%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B-97fbc472-c603-9d90-91d0-1166d1d9f4b5)  
  
Linuxの場合:  
ターミナルを開き、隠しフォルダが格納されているフォルダに`cd`してから、`ls -a`コマンドを実行します。  
  
また、Freecivをインストールしたものの、一度も起動していない場合は、`.freeciv`が存在しない場合があります。  
その場合は、一度Freecivを起動して、終了してから確認してみてください。
## 4. ルールセットフォルダを格納する
前項で見つけた`.freeciv`フォルダの中のバージョンフォルダに、取り出したルールセットフォルダと`.serv`ファイルを入れます。  
例えば、Freeciv v3.1.2がインストールされている場合、バージョンフォルダは`.freeciv/3.1`です。  
バージョンフォルダが存在しない場合は、新しく作成してください。
## ルールセットで遊ぶ
ゲーム開始前に、ルールセット設定で当該ルールセットを選択するか、  
サーバーで`rulesetdir （当該ルールセット名）`コマンドを実行してルールセットを適用します。
