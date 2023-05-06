import solver as solv
import problem_parking as prob_park
import solverAMPL as solv_ampl

distance =  [[0, 1.5, 1, 1.1, 2.3, 1.9, 2.7, 0.4], 
           [1.5, 0, 0.7, 0.85, 1.9, 1.5, 2.1, 1.6], 
           [1, 0.7, 0, 0.19, 1.4, 1, 1.7, 1.2], 
           [1.1, 0.85, 0.19, 0, 1.4, 1.1, 1.8, 1.1], 
           [2.3, 1.9, 1.4, 1.4, 0, 0.55, 1.3, 2.4], 
           [1.9, 1.5, 1, 1.1, 0.55, 0, 0.9, 2.1], 
           [2.7, 2.1, 1.7, 1.8, 1.3, 0.9, 0, 2.4], 
           [0.4, 1.6, 1.2, 1.1, 2.4, 2.1, 2.4, 0]] 

surface = [3000, 2000, 20000,800,4000,3600,25550,875]

distance_depot = [[2.1],
	    [1.75],
	    [1.45],
        [1.1],
        [0.7],
        [1],
	    [0.125],
	    [2.25]]
CM_neige = 15
coutKM =2

solveurAMPL = solv_ampl.SolverAmpl()
probleme = prob_park.ParkingProb(distance,distance_depot,surface,CM_neige,coutKM)
print(probleme.matrice_distance)

print(probleme.compter_nbr_surface())
print(probleme.compter_nbr_parking())
print(probleme.compter_nbr_distance_depot())
try:
    probleme.valider_probleme()
except Exception as e:
    print(e)
#a= solveurAMPL.solve(probleme)
#print(a)