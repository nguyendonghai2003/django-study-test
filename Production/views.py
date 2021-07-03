from django.shortcuts import render
from django.http import HttpResponse

from .models import Machine

def IndexView(request):
    return render(request,'Production/index.html')

def MachineListView(request):
    machine_list = Machine.objects.all()
    context = {'machine_list':machine_list}
    return render(request, 'Production/machine_list.html', context)

def MachineDetailView(request, machine_id):
    machine = Machine.objects.get(pk = machine_id)
    context = {'machine':machine}
    return render(request, 'Production/machine_details.html', context)

def MachineCreateView(request):
    pass
    return HttpResponse("Create")