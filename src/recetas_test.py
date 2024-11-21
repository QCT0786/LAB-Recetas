from recetas import *

def test_lee_recetas(ruta_archivo: str):
    """
    Función para probar la implementación de lee_recetas.
    
    Args:
        ruta_archivo (str): Ruta del archivo CSV con las recetas.
    """
    try:
        # Llamar a la función principal para leer las recetas
        recetas = lee_recetas(ruta_archivo)
        
        # Mostrar los resultados obtenidos
        print(f"Se han leído {len(recetas)} recetas del archivo '{ruta_archivo}':\n")
        for receta in recetas:
            print(receta)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta especificada: {ruta_archivo}")
    except ValueError as e:
        print(f"Error de formato en el archivo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    test_lee_recetas("data//recetas.csv")