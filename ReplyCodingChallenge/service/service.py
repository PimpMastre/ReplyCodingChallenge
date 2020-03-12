from model.developer import Developer
from model.project_manager import ProjectManager


class Service():
    def __init__(self, filename):
        self.__filename = filename
        self.__width = 0
        self.__height = 0
        self.__office_space = []
        self.__developers = []
        self.__project_managers = []

    def read_from_file(self):
        file = open(self.__filename, 'r')

        # read matrix
        sizes = file.readline().strip().split(' ')
        self.__width, self.__height = int(sizes[0]), int(sizes[1])
        self.__office_space = [['\0' for x in range(self.__width)] for y in range(self.__height)]  # init matrix w/ NULL
        for i in range(self.__height):
            line = file.readline().strip()
            for j in range(len(line)):
                self.__office_space[i][j] = line[j]

        # read developers
        number_of_developers = int(file.readline().strip())
        for i in range(number_of_developers):
            dev_line = file.readline().strip().split(' ')

            company = dev_line[0]
            bonus = int(dev_line[1])
            skills = dev_line[2:]
            self.__developers.append(Developer(company, bonus, skills))

        # read project managers
        number_of_project_managers = int(file.readline().strip())
        for i in range(number_of_project_managers):
            pm_line = file.readline().strip().split(' ')

            company = pm_line[0]
            bonus = int(pm_line[1])
            self.__project_managers.append(ProjectManager(company, bonus))

    def get_office_sizes(self):
        return self.__width, self.__height

    def get_office_space(self):
        return self.__office_space

    def get_developers(self):
        return self.__developers

    def get_project_managers(self):
        return self.__project_managers

    @staticmethod
    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        if len(lst3) == 0 :
            return 0
        return lst3

