class settings:
    __TIN = ""
    __account = ""
    __cor_account = ""
    __BIC = ""
    __property_type = ""

    #ИНН
    @property
    def TIN(self):
        return self.__TIN
    
    @TIN.setter
    def TIN(self, value: str):
        """
            Полное наименование
        Args:
            value (str): _description_

        Raises:
            Exception: _description_
        """
        if not isinstance(value, str) or len(value.strip())!=12: #если длина без лишних пробелов не совпадает с таковой у ИНН
            raise Exception("Некорректный аргумент!")
        
        self.__TIN = value.strip()
    
    #счет
    @property
    def account(self):
        return self.__account
    
    @account.setter
    def account(self, value: str):
        if not isinstance(value, str) or len(value.strip())!=11:
            raise Exception("Некорректный аргумент!")
        
        self.__account = value.strip()
    
    #кор_счет
    @property
    def cor_account(self):
        return self.__cor_account
    
    @cor_account.setter
    def cor_account(self, value: str):
        if not isinstance(value, str) or len(value.strip())!=11:
            raise Exception("Некорректный аргумент!")
        
        self.__cor_account = value.strip()
    
    #БИК
    @property
    def BIC(self):
        return self.__BIC
    
    @BIC.setter
    def BIC(self, value: str):
        if not isinstance(value, str) or len(value.strip())!=9:
            raise Exception("Некорректный аргумент!")
        
        self.__BIC = value.strip()
    
    #вид собственности
    @property
    def property_type(self):
        return self.__property_type
    
    @property_type.setter
    def property_type(self, value: str):
        if not isinstance(value, str) or len(value.strip())!=5:
            raise Exception("Некорректный аргумент!")
        
        self.__property_type = value.strip()