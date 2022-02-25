import bcrypt


class Password:
    @staticmethod
    def hash(password):
        utf8_password = password.endcode("utf-8")
        hashed = bcrypt.hashpw(utf8_password, bcrypt.gensalt())
        return hashed

    @staticmethod
    def check_password(password, hashed):
        if bcrypt.checkpw(password, hashed):
            return True
        else:
            return False
