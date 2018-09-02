from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from customuser.forms import RegistrationForm, EditUserForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect(reverse('home'))
        else:
            print("Deam")
            return redirect(reverse('home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'sign.html', args)


@login_required()
def view_profile(request):
    user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
        return redirect(reverse('view_profile'))
    else:
        user_form = EditUserForm(instance=request.user)
        args = {'form': user_form}
        return render(request,  'personal_page.html', args)

