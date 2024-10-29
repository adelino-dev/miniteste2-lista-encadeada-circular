class Membro:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._proximo = self
    
    def get_nome(self):
        return self._nome
    
    def get_email(self, email):
        return self._email
    
    def get_proximo(self, proximo):
        return self._proximo
    
    def set_nome(self, nome):
        self._nome = nome
    
    def set_email(self, email):
        self._email = email
    
    def set_proximo(self, proximo):
        self._proximo = proximo