

from hello.models import Person



from faker import Factory


fake= Factory.create()


def run():
for _ in range(10):
	Person(firstName = fake.name()).save()