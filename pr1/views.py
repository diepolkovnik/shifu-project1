from django.shortcuts import render, redirect
from pr1.models import zadanie

# Create your views here.
def cyber_forum_view(request):
    f = request.GET.get('context_value', '')
    f_2 = request.GET.get('title_value', '')
    f_3 = request.GET.get('slug_value', '')
    if str(f) != '' or str(f_2) != ''or str(f_3) != '':
        i = zadanie.objects.create(context=f, title=f_2, slug=f_3)
        i.save()

    return render(request, 'admin_add.html')

def add(request):
    f = request.GET.get('context_value', '')
    f_2 = request.GET.get('title_value', '')
    f_3 = request.GET.get('slug_value', '')
    if str(f) != '' or str(f_2) != '' or str(f_3) != '':
        i = zadanie.objects.create(context=f, title=f_2, slug=f_3)
        i.save()

    return render(request, 'admin/add.html')
def admin(request):

    return render(request, 'admin/admin.html' )

def article(request):
    y = zadanie.objects.values_list().values()
    context = {
        'context_value': y,
    }
    return render(request, 'admin/article.html', context)

def main_page(request):
    y = zadanie.objects.values_list().values()
    context = {
        'context_value': y,
    }
    return render(request, 'main_page.html', context)

def articles_delete(request, context):
    obj = zadanie.objects.get(context=context).delete()
    return redirect('http://127.0.0.1:8000/admin/articles/')

def rabota(request, j):
    y = zadanie.objects.filter(slug=j).values_list()
    template = "template.html"
    context = {
        'context': y[0][1],
        'title': y[0][2]
    }
    return render(request, template, context)

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # email = form.cleaned_data['emal']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'registration/index.html')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)


def send_email(request, email, username):
    subject = 'Thank you'
    message = 'http://127.0.0.1:8000/email_conf/' + username + '/'
    from_email = settings.EMAIL_HOST_USER
    to_list = [email]
    send_mail(subject, message, from_email, to_list)
    return HttpResponse("Message was sent.")


def login_new_func(request):
    username = request.GET.get('user_value', '')
    password = request.GET.get('pass_value', '')
    email = request.GET.get('email_value', '')

    if username != '' and password != '' and email != '':
        user = User.objects.create_user(username, email, password, is_active = 0)
        send_email(request, email, username)
        user.save()

    return render(request, 'Login.html')


def check_from_email(request, user_login):
    user2 = User.objects.get(username=user_login)
    user2.is_active = 1
    user2.save()
    return redirect('http://127.0.0.1:8000/accounts/login/')

def articles_edit(request, slug):
    y = zadanie.objects.filter(slug=slug).values_list()
    context = {
        'context': y[0][1],
        'title': y[0][2],
        'slug': y[0][3]
    }

    return render(request, 'admin/edit.html', context)