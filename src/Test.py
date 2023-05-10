import unittest

import problem as prob
import solver as solv
import problem_parking as prob_park
import solverAMPL as solv_ampl
import solverMiniZinc as solv_mini
import donnees as donne
import copy 

class TestClass(unittest.TestCase): 

### Test tout les instances des classes#####
    def test_instance_Problem(self):
        a = prob.Problem()
        self.assertTrue(isinstance(a,prob.Problem))

    def test_instance_Solver(self):
        b = solv.Solver()
        self.assertTrue(isinstance(b,solv.Solver))

    def test_instance_problem_parking(self):
        c = prob_park.ParkingProb()
        self.assertTrue(isinstance(c,prob_park.ParkingProb))
        self.assertTrue(isinstance(c,prob.Problem))

    def test_instance_SolverAmpl(self):
        d = solv_ampl.SolverAmpl()
        self.assertTrue(isinstance(d,solv_ampl.SolverAmpl))
        self.assertTrue(isinstance(d,solv.Solver))
    
    def test_instance_SolverMiniZinc(self):
        e = solv_mini.SolverMiniZinc()
        b = solv.Solver()
        self.assertTrue(isinstance(e,solv_mini.SolverMiniZinc))
        self.assertTrue(isinstance(e,solv.Solver))

    #Test les solveurs 
    def test_solver_solverAMPL(self):
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
        a = solveurAMPL.solve(probleme)
        self.assertTrue(isinstance(probleme,prob_park.ParkingProb))
        self.assertIsInstance(a,tuple)

        

if __name__ == '__main__':
    unittest.main()


































    
###Visuellement ce que fait la classe###
#####Test class problem####
try:
    a = prob.Problem()
    print(isinstance(a,prob.Problem))
except:
    print("Problème d'instance dans la classe Problem")


#####Test class solver###
try:
    b = solv.Solver()
    print(isinstance(b,solv.Solver))
except:
    print("Problème d'instance dans la classe solver")



####Test class problem_parking####
try:
    c = prob_park.ParkingProb()
    print("Instance de la classe ParkingProb    :",isinstance(c,prob_park.ParkingProb))
    print("Instance de la classe Problem        :",isinstance(c,prob.Problem))
except:
    print("Problème d'instance dans la classe ParkingProb")



####Test class SolverAMPL####
try:
    d = solv_ampl.SolverAmpl()
    print("Instance de la classe SolverAmpl     :", isinstance(d,solv_ampl.SolverAmpl))
    print("Instance de la class Solver          :",isinstance(d,solv.Solver))
except:
    print("Problème d'instance dans la classe SolverAMPL")


####Test class SolverAMPL####
try:
    d = solv_mini.SolverMiniZinc()
    print("Instance de la classe SolverMiniZinc :", isinstance(d,solv_mini.SolverMiniZinc))
    print("Instance de la class Solver          :",isinstance(d,solv.Solver))
except:
    print("Problème d'instance dans la classe SolverMinizinc")