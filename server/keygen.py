import random


class Key:
    @staticmethod
    def generate(length):
        result = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length)))
        return result

    def check_unique(code):
        """
        Check if the code provided is unique
        import database and write a method to check if provided code is unique or not.
        The code will be checked from table 2
        """
        pass
