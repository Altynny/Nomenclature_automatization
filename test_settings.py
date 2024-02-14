from settings import settings
from settings_manager import  settings_manager
import unittest
import os

class test_settings(unittest.TestCase):
    
    def test_check_create_manager(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        # Действие
        
        # Проверки
        print(str(manager1.number))
        print(str(manager2.number))
    
        assert manager1.number == manager2.number
    #
    # Проверить корректность заполнения полей
    #
    def test_check_TIN(self):
        # Подготовка
        item = settings()
        
        # Действие
        item.TIN = "000000000000  "
        
        # Проверка
        assert item.TIN == "000000000000"
    
    def test_check_account(self):
        item = settings()
        
        item.account = "00000000000  "
        
        assert item.account == "00000000000"
    
    def test_check_cor_account(self):
        item = settings()
        
        item.cor_account = "00000000000  "
        
        assert item.cor_account == "00000000000"
    
    def test_check_BIC(self):
        item = settings()
        
        item.BIC = "000000000  "
        
        assert item.BIC == "000000000"
    
    def test_check_BIC(self):
        item = settings()
        
        item.BIC = "000000000  "
        
        assert item.BIC == "000000000"
    
    def test_check_property_type(self):
        item = settings()
        
        item.property_type = "00000  "
        
        assert item.property_type == "00000"
    
        
    def test_check_manager_convert(self):
        # Подготовка
        manager = settings_manager()
        manager.open("settings.json")
         
        # Действие
        manager.convert()       
        
        # Проверка    
        
    def test_check_open_settings(self):
        # Подготовка
        manager = settings_manager()
        
        # Действие
        result = manager.open("settings.json")
        
        # Проверка
        print(manager.data)
        assert result == True