#指示書
#ブラウザから呼び出されてviewに指示投げる
#入力：リクエスト(ブラウザでアクセスするurl)
#出力：どういう画面を作るか

from django.urls import path
# 同じ階層のhelloworldfunctionからhelloworldfunction(メソッド)を呼び出す(メソッド呼び出し)
from .views import helloworldfunction

# どういう画面を返すか=funcrionベースで指定。(functionベースとclassベースで呼び出す方法2種類ある。)
urlpatterns = [
    #views.pyの中のhellofunctionを返す
    #入力：world/
    #出力：同じ階層のviews.pyのhelloworldfunctionメソッド

    path('world/', helloworldfunction),
]
