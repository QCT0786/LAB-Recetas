from recetas import *

def lee_recetas_t(ruta_archivo: str)->list[Receta]:
    print("Probando lee recetas")
    lee_recetas(ruta_archivo)
    return lee_recetas(ruta_archivo)

def receta_mas_barata_test(recetas: list[Receta], conj_tipos: set[str], n:int = None):
   print("Probando receta mas barata") 
   receta_mas_barata(recetas, conj_tipos, n)

def total_recetas_por_tipo_t(recetas:list[Receta])->dict[str]:
    print("Probando total recetas por tipo")
    print(total_recetas_por_tipo(recetas))

def lista_de_recetas_por_ingredientes_t(recetas: list[Receta])->dict[str]:
    print("Probando lista de recetas por ingredientes")
    print(lista_de_recetas_por_ingredientes(recetas))

if __name__ == "__main__":
    recetas = lee_recetas_t("data//recetas.csv")
    receta_mas_barata_test(recetas, {"Postre", "Entrante", 5})
    total_recetas_por_tipo_t(recetas)
    lista_de_recetas_por_ingredientes_t(recetas)