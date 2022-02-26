import random


class Key:
    @staticmethod
    def generate():
        random.seed(number)
        result = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length)))
        return result

    def check_unique(code):
        """
        Check if the code provided is unique
        """
        pass
