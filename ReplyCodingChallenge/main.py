from service.service import Service


def start():
    service = Service("data/a_solar.txt")
    service.read_from_file()


start()
