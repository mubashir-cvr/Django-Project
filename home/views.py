from django.shortcuts import render
from .models import Service, Servicer, Users


def index(request):
    users = Servicer.objects.all()
    services = Service.objects.all()
    # service = Service.objects.get(id=1).servicer_set.all()
    # print(service)
    index = 1
    for user in users:
        first = ''
        if index % 3 == 1:
            first = 'first'
        else:
            first = ''
        index += 1
        setattr(user, 'first', first)
    for service in services:
        servicercount = service.servicer_set.all().filter(isActive=True).filter(pendingJob__lte=2).count()
        setattr(service, 'servicercount', servicercount)
    context = {
        'servicers': users,
        'services': services
    }
    return render(request, 'index.html', context)


def userdetails(request, id):
    user = Users.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, 'userDetails.html', {'user': context})
