import hello.loadData

from hello.models import  Person

Person.objects.all().delete()


loadData.run()