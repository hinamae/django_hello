# README

## djangoとは？

- 普通のwebサイト
もう食事が出来上がっているので、それを出す

- django
    1.  url.pyが味噌ラーメンを作れと指示を出す
    2.  view.pyが指示を受け取る
    3. views.pyはtemplateをもってくる(大盛りの丼ぶりをもってくる)
    4. views.pyはmodels.pyから食材を持ってくる

## youtubeの例

youtubeはdjangoで作られている

### 最新の動画が見たい。
1. https://youtube.com/latest(リクエスト)→viewのA
2. urls.pyは新しい動画を見れるようなwebサイトを作れとviews.pyに指示
3. 動画を並べるtemplateをもってくる。models.pyからDBに入っている新しい動画データを引っ張ってくる。



### 自分のprofileをみたい
1. https://youtube.com/profile/taro→viewのB
2. urls.pyはtaroというユーザのprofileの画面を作れとview.pyに指示。
3. templateの中からユーザの情報を表示するのに適したhtmlファイルを持ってくる。models.pyでDBのなかからtaroというuserを引っ張ってくる。


## localhost

127.0.0.1
(localhost)

- 身内だけで参照できるIPアドレス
- localhostをブラウザの窓に打ち込むこと＝自分のPCにアクセスする

### ポート
デフォルト80番(http)

## django

init.py=pythonパッケージが入っていることを認識させる
wsgi.py=webサーバを動かすためのもの。pythonプログラムとwebサーバの仲介。djangoとサーバを繋ぐ。


## 最小プログラム

リクエストを受け取って、リクエストを返す

## view

urls.pyでのviewの呼び出し方には、
- function based view 
- class based view
の2種類ある。

urls.py
```
path('url' , [function指定/class指定])

```


### function based view
最新の設備がないキッチンみたいな。
古いキッチン。
細かい指示がしやすい。

### class based view
最新のシステムキッチンみたいな。
簡単に作れるけど設定覚えるのめんどい。
細かい指示に耐えられないことも。

## BASE_DIRとは

- BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

- (プロジェクトが入っているパス(settings.pyが入っているパス(絶対パスを指定している))

(os.path.dirname(a)によって、「aの一階層上の(aが入っているディレクトリ)」という意味になる)

### 結論
BASE_DIRはmanage.pyが入っているディレクトリのフルパス


## アプリ

### アプリが必要な理由?
<例：ECサイト>

画面：たくさん必要
- xx.com/pay(支払い画面)
- xx.com/item(商品画面)
- xx.com/qa(QA画面)

views.pyがやりとりするtemplateもmodelsも膨大になる。

templateもmodelsも機能ごとにごっちゃになった、ファイルをたくさん持たなければならなくなる。
整理しづらい。。。

### アプリを作ると。。。

プロジェクトのurls.pyがアプリにリクエストを振り分ける。

それぞれのviewがおのおののmodelとtemplateを使用して、画面をかえす。


まあ、小さいサイトならappを使用しなくても作れてしまう。

### 全体の流れ

アプリの中にはデフォルトでは、urls.pyが入っていない。
がしかし作るのが定石。


プロジェクトの中にはview.py,models.pyは入っていない。
プロジェクトの中でゴタゴタデータを入れていく、という流れは想定されていない。
それぞれのアプリの中でmodelやtemplateから画面を作成するという流れが想定されている。

### urls.py
リクエストとして、https://aaa/com/news/priceがきたとする。
#### 1.プロジェクトのurls.py
urlpatterns =[news , アプリのurl]
- 入力：リクエストのアプリのurlまで
- 出力：アプリのurl

リクエストからurlを受け取り、当てはまるアプリのurlを呼び出す。
#### 2.アプリのurls.py
urlpatterns=[price ,view]
- 入力：アプリのurl
- 出力：view

プロジェクトのurls.pyからurlを受け取り、当てはまるviewを呼び出す。


(viewの呼びだしはメソッドorクラス)

## アプリ作成
http://localhost:8000/hello/world/
にアクセスできるようになった。
