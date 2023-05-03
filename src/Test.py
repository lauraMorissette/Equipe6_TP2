import unittest

import problem as prob
import solver as solv
import problem_parking as prob_park
import solverAMPL as solv_ampl
import solverMiniZinc as solv_mini


a = prob.Problem()
b = solv.Solver()
c = prob_park.ParkingProb()
d = solv_ampl.SolverAmpl()
e = solv_mini.SolverMiniZinc()


###Cette classe Test tout les instances des classes#####
class TestClass(unittest.TestCase): 

    def test_instance_Problem(self):
        self.assertTrue(isinstance(a,prob.Problem))
    def test_instance_Solver(self):
        self.assertTrue(isinstance(b,solv.Solver))
    def test_instance_problem_parking(self):
        self.assertTrue(isinstance(c,prob_park.ParkingProb))
        self.assertTrue(isinstance(c,prob.Problem))
    def test_instance_SolverAmpl(self):
        self.assertTrue(isinstance(d,solv_ampl.SolverAmpl))
        self.assertTrue(isinstance(d,solv.Solver))
    def test_instance_SolverMiniZinc(self):
        self.assertTrue(isinstance(e,solv_mini.SolverMiniZinc))
        self.assertTrue(isinstance(e,solv.Solver))


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