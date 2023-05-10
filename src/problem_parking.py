import copy
import problem
import donnees
import os

class ParkingProb(problem.Problem):

    #On intialise la classe ParkingProb, elle Hérite de la classe Problem
    #La classe a comme attribut les différentes matrice nécessaire à la résolution du problème
    def __init__(self, matrice_distance=[[]], matrice_Depot=[[]],matrice_surface_parking=[[]], cm_neige =0, cout_KM=0):
        super(ParkingProb,self).__init__()
        try : 
            self._validation_matrice_(matrice_distance, matrice_Depot, matrice_surface_parking)
            self.matrice_distance = copy.deepcopy(matrice_distance)
            self.matrice_depot = copy.deepcopy(matrice_Depot)
            self.matrice_surface = copy.deepcopy(matrice_surface_parking)
            self.cm_neige = cm_neige
            self.cout_KM = cout_KM
        except Exception as e:
            print(e)
            os._exit


    def _validation_matrice_(self, m1, m2, m3):
        longueur1 = len(m1)
        longueur2 = len(m2)
        longueur3 = len(m3)
        if longueur1 == longueur2 == longueur3: 
            pass
        else :
            raise Exception('Les matrices donnée en entrée ne sont pas compatible')

    #compte la longueur de la matrice parking
    def compter_nbr_parking(self):
        return len(self.matrice_distance)
    
    #compte la longueur de la matrice surface
    def compter_nbr_surface(self):
        return len(self.matrice_surface)
    
    #compte la longueur de la matrice distance 
    def compter_nbr_distance_depot(self):
        return len(self.matrice_depot)
