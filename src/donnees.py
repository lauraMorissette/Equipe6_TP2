
class Distance():

    def __init__(self) -> None:
        self.distance_matrix = [[0, 1.5, 1, 1.1, 2.3, 1.9, 2.7, 0.4],
           [1.5, 0, 0.7, 0.85, 1.9, 1.5, 2.1, 1.6],
           [1, 0.7, 0, 0.19, 1.4, 1, 1.7, 1.2],
           [1.1, 0.85, 0.19, 0, 1.4, 1.1, 1.8, 1.1],
           [2.3, 1.9, 1.4, 1.4, 0, 0.55, 1.3, 2.4],
           [1.9, 1.5, 1, 1.1, 0.55, 0, 0.9, 2.1],
           [2.7, 2.1, 1.7, 1.8, 1.3, 0.9, 0, 2.4],
           [0.4, 1.6, 1.2, 1.1, 2.4, 2.1, 2.4, 0]]
        
    def get_matrice():
        return Distance.distance_matrix
    
    def get_longueur_matrice():
        pass