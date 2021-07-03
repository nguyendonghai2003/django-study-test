import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',"Plastic.settings")
django.setup()


from Production.models import Machine

# Create
"""
may = Machine(machine_code = "I7", machine_name = "Test machine", 
location = "X2", clamping_force = "50")
may.save()"""

#update

sua_may = Machine.objects.filter(machine_name__contains = "Test")

for item in sua_may:
    item.machine_name = str(item.machine_code) + str(item.location) + str(item.clamping_force)
    item.save()
    print(item, item.machine_name)


#delete
"""xoa_may = Machine.objects.filter(machine_code__contains = "7")
xoa_may.delete()"""

# read
list_machine = Machine.objects.all()

for machine in list_machine:
    print(machine.machine_name)
    print(machine.machine_code)
    print(machine.location)
    print(machine.clamping_force)

