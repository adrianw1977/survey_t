from django.shortcuts import render, redirect, HttpResponse
# CONTROLLER !!!!
# Create your views here.
def index(request):
	print ("*"*100)
	return render(request, "first_app/index.html" )

def show(request):
	print(request.method)
	return render(request,
		'first_app/show_users.html')

def create(request):
	if request.method == "POST":
		print ('*'*50)
		print (request.POST)
		print ('*'*50)
		request.session['name1'] = request.POST['first_name']
		request.session['name2'] = request.POST['last_name']
		request.session['city'] = request.POST['city']
		request.session['fav_lang'] = request.POST['fav_lang']
		return redirect('/show')

	else:
		return redirect('/')
