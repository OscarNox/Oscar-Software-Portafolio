import pandas as pd

def cargar_datos(ruta):
    datos = pd.read_csv(ruta)
    return datos

def ventas_totales(datos):
    return datos["ventas"].sum()

def producto_mas_vendido(datos):
    return datos.groupby("producto")["ventas"].sum().idxmax()

def main():

    archivo = "data/ventas.csv"

    datos = cargar_datos(archivo)

    print("Ventas totales:", ventas_totales(datos))
    print("Producto más vendido:", producto_mas_vendido(datos))

if __name__ == "__main__":
    main()