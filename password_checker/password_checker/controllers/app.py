from django.shortcuts import render
from ..forms.form import MainForm
from ..utils.check_password import check_password


def password_checker(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            strength_message = check_password(password)
            return render(request, 'views/results.html', {'strength_message': strength_message})
    else:
        form = MainForm()

    return render(request, 'views/index.html', {'form': form})
