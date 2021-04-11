import uuid, random
#@todo: how to do this in the database?


#@todo: we shouldnt repeat the word generator in the class methods
class BloxGenerator:
    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def get_sshprivate_availability():
        return BloxGenerator.weighted_choice([("available", .4), ("in_use", .55), ("lost", .05)])

    @staticmethod
    def generate_random_cryptos():
        return random.choice(env.cryptos)

    @staticmethod
    def generate_random_numericstring():
        return {'lat': random.uniform(-180, 180), 'long': random.uniform(-90, 90)
