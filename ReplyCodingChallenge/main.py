from service.service import Service
from random import randint

from utils.utils import getTotalScore


def start():
    service = Service("data/e_igloos.txt")
    service.read_from_file()
    sizes = service.get_office_sizes()
    for i in range(sizes[0] * sizes[1]):
        print(i)
        this_problem_is_too_hard_so_we_gave_up(service.get_office_sizes(),
                                               service.get_office_space(),
                                               service.get_developers(),
                                               service.get_project_managers())


def this_problem_is_too_hard_so_we_gave_up(sizes, office, d, p):
    developers = []
    project_managers = []
    for i in range(len(d)):
        developers.append([d[i], (-1, -1)])
    for i in range(len(p)):
        project_managers.append([p[i], (-1, -1)])

    placements = dict()
    devs_placed = 0
    mans_placed = 0

    for i in range(sizes[1]):
        for j in range(sizes[0]):
            cell = office[i][j]
            if cell == '_':
                if devs_placed == len(developers):
                    continue
                rand = randint(0, len(developers) - 1)
                while developers[rand][1] != (-1, -1):
                    rand = randint(0, len(developers) - 1)
                developers[rand][1] = (i, j)
                devs_placed += 1
                placements[(i, j)] = developers[rand][0]
            elif cell == 'M':
                if mans_placed == len(project_managers):
                    continue
                rand = randint(0, len(project_managers) - 1)
                while project_managers[rand][1] != (-1, -1):
                    rand = randint(0, len(project_managers) - 1)
                project_managers[rand][1] = (i, j)
                mans_placed += 1
                placements[(i, j)] = project_managers[rand][0]

    maximum = getTotalScore(sizes, office, placements)
    try:
        out = open('output/e/' + str(maximum) + '.txt', 'r')
    except:
        output_file = open('output/e/' + str(maximum) + '.txt', 'w+')
        for dev in developers:
            if dev[1] != (-1, -1):
                output_file.write(str(dev[1][0]) + ' ' + str(dev[1][1]) + '\n')
            else:
                output_file.write('X\n')

        for pm in project_managers:
            if pm[1] != (-1, -1):
                output_file.write(str(pm[1][0]) + ' ' + str(pm[1][1]) + '\n')
            else:
                output_file.write('X\n')


start()
