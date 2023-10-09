from faker import Faker

fake = Faker()

print(fake.first_name())

for i in fake.__dir__():
    print(i)
