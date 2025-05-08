import pandas as pd

def crear_dataframe():
    datos = {
        'Nombre': ['Ana', 'Luis', 'María', 'Carlos'],
        'Edad': [28, 34, 25, 40]
    }
    df = pd.DataFrame(datos)
    print("DataFrame original:")
    print(df)

    promedio_edad = df['Edad'].mean()
    print(f"\nEdad promedio: {promedio_edad:.2f}")

if __name__ == "__main__":
    crear_dataframe()
