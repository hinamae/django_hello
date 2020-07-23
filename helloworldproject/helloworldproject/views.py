#djangoのhttpモジュールの中からHttpResponseクラスをインポートする
from django.http import HttpResponse
#めっちゃいろんな機能が入っているクラスであるTemplateViewをインポートする
from django.views.generic import TemplateView

#リクエストを受け取って、クラスから新しくオブジェクトを作って返してあげる
def helloworldfunction(request):
    returnobject = HttpResponse('<h1>hello!world<h1>')
    return returnobject


#クラスの場合、TemplateViewクラスを継承するという場合が多い
class HelloWorldView(TemplateView):
    #TemplateViewクラスにおいては、template_nameを指定するだけで、HelloWorldViewを呼び出した時に、hello.htmlを呼び出すことができる
    #TemplateViewクラスの便利機能！！
    template_name= 'hello.html'