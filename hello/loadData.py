

from .models import Person



from faker import Factory


fake= Factory.create()



for _ in range(10):
	Person(firstName = fake.name()).save()