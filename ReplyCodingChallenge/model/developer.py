class Developer():
    def __init__(self, company, bonus, skills):
        self.__company = company
        self.__bonus = bonus
        self.__skills = skills

    def get_company(self):
        return self.__company

    def get_bonus(self):
        return self.__bonus

    def get_skills(self):
        return self.__skills

    def set_company(self, value):
        self.__company = value

    def set_bonus(self, value):
        self.__bonus = value

    def set_skills(self, value):
        self.__skills = value
