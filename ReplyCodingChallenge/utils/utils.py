from model.developer import Developer


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def union(lst1, lst2):
    return lst1 + lst2


def getWorkPotential(developer1, developer2):
    inters = intersection(developer1.get_skills(), developer2.get_skills())
    uni = union(developer1.get_skills(), developer2.get_skills())

    return len(inters) * (len(uni) - len(inters))


def getBonusPotential(developer1, developer2):
    if developer1.get_company() == developer2.get_company():
        return developer1.get_bonus() * developer2.get_bonus()
    return 0


def getTotalPotential(replyer1, replyer2):
    bonusPotential = getBonusPotential(replyer1, replyer2)
    workPotential = 0
    if isinstance(replyer1, Developer) and isinstance(replyer2, Developer):
        workPotential += getWorkPotential(replyer1, replyer2)
    return bonusPotential + workPotential

def getTotalScore(sizes, matrix, map):
    sum = 0
    for i in range(sizes[0] - 1):
        for j in range(sizes[1] - 1):
            cell = matrix[i][j]

            #searching right cell
            if matrix[i][j + 1] != 0:
                sum += getTotalPotential(
                                        map[(i, j)],
                                        map[i,j + 1]
                                         )

            #searching bottom cell
            if matrix[i + 1][j] != 0:
                sum += getTotalPotential(
                                        map(i, j),
                                        map[i + 1, j]
                                        )

    return sum