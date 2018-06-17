from django.shortcuts import render, redirect
from reg_log.models import zadanie

# Create your views here.
def cyber_forum_view(request):
    f = request.GET.get('context_value', '')
    f_2 = request.GET.get('title_value', '')
    f_3 = request.GET.get('slug_value', '')
    if str(f) != '' or str(f_2) != ''or str(f_3) != '':
        i = zadanie.objects.create(context=f, title=f_2, slug=f_3)
        i.save()

    return render(request, 'admin_add.html')


def main_page(request):
    y = zadanie.objects.values_list().values()
    context = {
        'context_value': y,
    }
    return render(request, 'main_page.html', context)