from django.shortcuts import render
from newsapi import NewsApiClient
from .forms import newsform
# Create your views here.
def index(request):
    scrr = 'the-hindu'
    newsapi = NewsApiClient(api_key = '7fbe8a43036d44a198e94b58be8d85a1')
    forms = newsform()
    if request.method == 'POST':
        forms = newsform(request.POST)
        if forms.is_valid():
            news = forms.cleaned_data['news']
            print(news)
            if('verge' in news):
                scrr = 'the-verge'
            elif('bcc' in news):
                scrr = 'bbc-news'
            elif('hindu' in news):
                scrr = 'the-hindu'
    top = newsapi.get_everything(sources=scrr,language='en')
 
    l = top['articles']
    desc=[]
    news=[]
    img=[]
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news,desc,img)
    context = {'mylist':mylist,'forms':forms}
    return render(request,'newsapp/news.html',context)