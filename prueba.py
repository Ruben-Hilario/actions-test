import pandas as pd

def crear_dataframe():
    datos = {
        'Nombre': ['Ana', 'Luis', 'María', 'Carlos'],
        'Edad': [28, 34, 25, 40]
    }
    df = pd.DataFrame(datos)
    df.to_csv('reporte_ejecucion.csv',index=False)
    print("DataFrame original:")
    print(df)

    promedio_edad = df['Edad'].mean()
    print(f"\nEdad promedio: {promedio_edad:.2f}")
    with open('reporte_resultados.txt', 'w') as f:
        f.write(f"Edad promedio: {promedio_edad:.2f}\n")
    print(f"\nEdad promedio: {promedio_edad:.2f} guardado en 'reporte_resultados.txt'")

if __name__ == "__main__":
    crear_dataframe()
