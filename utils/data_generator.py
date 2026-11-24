import random
from faker import Faker

faker = Faker("en_US")


class DataGenerator:

    @staticmethod
    def generate_random_email():
        return faker.email()

    @staticmethod
    def generate_random_password():
        return faker.password(12)

    @staticmethod
    def generate_random_name():
        return faker.name()

    @staticmethod
    def generate_random_price():
        return random.randint(100, 1000)

    @staticmethod
    def generate_random_description():
        return faker.sentence()

    @staticmethod
    def generate_random_location():
        return random.choice(('SPB','MSK'))

    @staticmethod
    def generate_random_genre_id():
        return random.randint(1, 11)

    @staticmethod
    def generate_random_movie_name():
        return faker.sentence(nb_words=4)

    @staticmethod
    def generate_random_city():
        return faker.city()

    @staticmethod
    def generate_random_img_url():
        return faker.image_url()

    @staticmethod
    def generate_random_negative_number():
        return random.randint(-100, -1)