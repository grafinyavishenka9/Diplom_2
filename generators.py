from faker import Faker


def generate_user_credentials():
    fake = Faker()
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
        }
