from passlib.context import CryptContext


class Encryption:
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )

    def encrypt_password(self, password):
        return self.pwd_context.encrypt(password)

    def check_encrypted_password(self, password, hashed):
        return self.pwd_context.verify(password, hashed)


encryption = Encryption()
