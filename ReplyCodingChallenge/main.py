from service.service import Service
from utils.utils import getTotalPotential

def start():
    service = Service("data/a_solar.txt")
    service.read_from_file()

    dev1 = Developer("Company", 300, [1, 2, 3])
    dev2 = Developer("Company", 300, [1, 2, 3])
    print(getTotalPotential(dev1, dev2))


start()
