#指示書
#ブラウザから呼び出されてviewに指示投げる
#入力：リクエスト(ブラウザでアクセスするurl)
#出力：どういう画面を作るか

from django.contrib import admin
from django.urls import path
#includeメソッドをインポート
from django.urls import include

#adminというリクエストが投げられると、admin画面を返す
# どういう画面を返すか=funcrionベースで指定。(functionベースとclassベースで呼び出す方法2種類ある。)
urlpatterns = [
    #helloにしたので、http://localhost:8000/hello/にアクセスするとadmin画面が出てくる
    path('admin/', admin.site.urls),
    #アプリへの繋ぎ込みのため
    #urlを渡す(今回このアプリ側にわたすurlはhelloとした。)
    #入力：http://localhost:8000/hello/world
    #出力：worldの部分(http://localhost:8000/hello/world)を、helloworldappアプリ(のurls.py)に返す
    path("hello/", include('helloworldapp.urls'))
]
