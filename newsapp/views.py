from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST)
    newsapi = NewsApiClient(api_key = '7fbe8a43036d44a198e94b58be8d85a1')
    top = newsapi.get_top_headlines(sources='the-hindu',language='en')
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
    context = {'mylist':mylist}
    return render(request,'newsapp/news.html',context)