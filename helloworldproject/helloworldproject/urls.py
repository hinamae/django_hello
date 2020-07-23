#指示書
#ブラウザから呼び出されてviewに指示投げる
#入力：リクエスト(ブラウザでアクセスするurl)
#出力：どういう画面を作るか

from django.contrib import admin
from django.urls import path
# 同じ階層のhelloworldfunctionからhelloworldfunction(メソッド)を呼び出す
from .views import helloworldfunction
# 同じ階層のhelloworldfunctionからHelloWorldViewクラスを呼び出す
from .views import HelloWorldView

#adminというリクエストが投げられると、admin画面を返す
# どういう画面を返すか=funcrionベースで指定。(functionベースとclassベースで呼び出す方法2種類ある。)
urlpatterns = [
    #helloにしたので、http://localhost:8000/hello/にアクセスするとadmin画面が出てくる
    path('hello/', admin.site.urls),
    #helloworld1のリクエストをもらった際には、helloworldfunctionを返す
    path('helloworld1/', helloworldfunction),
    #クラスで指定してブラウザに表示する場合には、as_view()メソッドで指定しなければならない。
    path('helloworld2/', HelloWorldView.as_view()),
]
