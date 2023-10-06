from faker import Faker

fake = Faker()

for i in fake.__dir__():
    print(i)
