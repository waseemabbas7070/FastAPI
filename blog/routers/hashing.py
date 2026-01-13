class Hash:
    # Utility class used for password hashing

    @staticmethod
    def bcrypt(password: str) -> str:
        # Hashes a plain-text password using bcrypt

        import bcrypt
        # bcrypt library for secure hashing

        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),  # bcrypt requires bytes
            bcrypt.gensalt()           # generate secure random salt
        ).decode('utf-8')              # store hash as string

        return hashed_password
        # Returns the hashed password
