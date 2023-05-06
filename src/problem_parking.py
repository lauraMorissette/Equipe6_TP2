import copy
import problem


#Hérite de la classe Problem
class ParkingProb(problem.Problem):
    def __init__(self, matrice_distance=[[]], matrice_surface_parking=[[]], cm_neige =0):
        super(ParkingProb,self).__init__()
        self.matrice_distance = copy.deepcopy(matrice_distance)
        self.matrice_surface = copy.deepcopy(matrice_surface_parking)
        self.cm_neige = cm_neige

    def compter_nbr_parking(self):
        return len(self.matrice_distance)
        