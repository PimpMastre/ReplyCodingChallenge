from service.service import Service
from utils.utils import getTotalPotential

def start():
    service = Service("data/a_solar.txt")
    service.read_from_file()

    devs = service.get_developers()
    print(devs[0],devs[2])
    print(getTotalPotential(devs[0], devs[2]))


start()
