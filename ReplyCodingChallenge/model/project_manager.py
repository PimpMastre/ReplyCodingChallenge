class ProjectManager():
    def __init__(self, company, bonus):
        self.__company = company
        self.__bonus = bonus

    def get_company(self):
        return self.__company

    def get_bonus(self):
        return self.__bonus

    def set_company(self, value):
        self.__company = value

    def set_bonus(self, value):
        self.__bonus = value
