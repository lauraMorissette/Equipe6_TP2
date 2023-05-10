import copy
import problem
import donnees

#Hérite de la classe Problem
class ParkingProb(problem.Problem):
    def __init__(self, matrice_distance=[[]], matrice_Depot=[[]],matrice_surface_parking=[[]], cm_neige =0, cout_KM=0):
        super(ParkingProb,self).__init__()
        self.matrice_distance = copy.deepcopy(matrice_distance)
        self.matrice_depot = copy.deepcopy(matrice_Depot)
        self.matrice_surface = copy.deepcopy(matrice_surface_parking)
        self.cm_neige = cm_neige
        self.cout_KM = cout_KM

    def compter_nbr_parking(self):
        return len(self.matrice_distance)
    
    def compter_nbr_surface(self):
        return len(self.matrice_surface)
    
    def compter_nbr_distance_depot(self):
        return len(self.matrice_depot)
