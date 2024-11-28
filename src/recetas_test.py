from recetas import *

def lee_recetas_t(ruta_archivo: str)->list[Receta]:
    print("Probando lee recetas")
    lee_recetas(ruta_archivo)
    return lee_recetas(ruta_archivo)

def receta_mas_barata_test(recetas: list[Receta], conj_tipos: set[str], n:int = None):
   print("Probando receta mas barata") 
   receta_mas_barata(recetas, conj_tipos, n)

if __name__ == "__main__":
    recetas = lee_recetas_t("LAB-Recetas//data//recetas.csv")
    receta_mas_barata_test(recetas, {"Postre", "Entrante", 5})