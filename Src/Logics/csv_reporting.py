from Src.Logics.reporting import reporting


class csv_reporting(reporting):
    
    def create(self, typeKey: str):
        super().create(typeKey)
        head = self.fields #заголовок как массив
        result = f"{';'.join(head)}\n" #добавляем элементы заголовка через разделитель

        # Исходные данные
        objects = self.data[ typeKey ] #получаем список объектов по ключу из словаря data
        
        # Список
        rows = [] #список строк
        
        #перебираем объекты в их списке
        for object in objects: 
            row = [] #строка, как массив атрибутов

            #берём имена атрибутов из заголовка
            for attribute_name in head:

                #получаем значение атрибута по имени и добавляем в строку-массив
                attr = str(getattr(object, attribute_name)) 
                row.append(attr)
                
            #добавляем массив атрибутов в виде строки с разделителем к массиву строк
            rows.append(';'.join(row)) 
        
        # Результат csv
        result+='\n'.join(rows) #добавляем строки, разделенные через символ перехода строки
        return result     