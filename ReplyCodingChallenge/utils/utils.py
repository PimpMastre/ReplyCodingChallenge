def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    if len(lst3) == 0:
        return 0
    return lst3


def union(lst1, lst2):
    return lst1 + lst2


@staticmethod
def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    if len(li_dif) == 0:
        return 0
    return li_dif


def getWorkPotential(developer1, developer2):
    intersection = intersection(developer1.get_skills(), developer2.get_skills())
    union = union(developer1.get_skills(), developer2.get_skills())

    return intersection * diff(union, intersection)


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