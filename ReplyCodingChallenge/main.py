from model.developer import Developer
from utils.utils import getTotalPotential

dev1 = Developer("Company",300,[1,2,3])
dev2 = Developer("Company",300,[1,2,3])
print(getTotalPotential(dev1, dev2))

