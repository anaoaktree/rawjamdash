

from hello.models import Person



from faker import Factory


fake= Factory.create()


def run():
	for _ in range(10):
		p= fake.simple_profile()
		Person(firstName = p["name"],userName=p["username"]).save()