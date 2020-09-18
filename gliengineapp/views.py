from django.shortcuts import render
#gliengineapps VIEWS

def adminkey(request):
	if request.method == 'POST':
		key = request.POST['key']

		if key == "magumbo":
			runrobomatrix()
			print("key Correcta")
			return redirect('watchlist')
		else:
			print("key Incorrecta")
			return redirect('watchlist')
