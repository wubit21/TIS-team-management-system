from django.shortcuts import render
# Create your views here.
def home_screen_view(request):

	context= {}
	
	#context['site']=site
	return render(request,"main/home.html", context)