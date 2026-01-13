import bcrypt
class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:
        
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),  
            bcrypt.gensalt()           
        ).decode('utf-8')             

        return hashed_password
        
