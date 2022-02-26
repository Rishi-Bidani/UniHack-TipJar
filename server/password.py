import bcrypt


class Password:
    @staticmethod
    def hash(password):
        utf8_password = password.encode()
        hashed = bcrypt.hashpw(utf8_password, bcrypt.gensalt())
        return hashed

    @staticmethod
    def check_password(password, hashed):
        if bcrypt.checkpw(password, hashed):
            return True
        else:
            return False
