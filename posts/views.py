from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts=[
{
	'author':'abrar',
	'title':'ahemd',
	'content':'some content',
	'date_created':'25 Aug 2017'
},
{
	'author':'abrar',
	'title':'ahemd',
	'content':'some content',
	'date_created':'25 Aug 2017'
}
]

context={'data':posts}
def home(request):
	return render(request,'posts/home.html',context=context)
	


def about(request):
	return render(request,'posts/about.html')
	#return HttpResponse("<h1> About page </h1>")
