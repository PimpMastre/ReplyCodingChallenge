class Service():


    def __init__(self, filename):
        self.__filename = filename
        


    @staticmethod
    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        if len(lst3) == 0 :
            return 0
        return lst3

    def get_wp(self, developer1, developer2):
