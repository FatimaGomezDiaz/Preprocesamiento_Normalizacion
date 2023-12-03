#Fatima Gomez Diaz
#941
#Realizar una función que normalice los datos usando Z-Score que reciba como parámetro un DataFrame y otro parámetro que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.

import pandas as pd

def normalizar_z_score_acuario(acuario_df, columnas_a_normalizar):
    df_normalizado = acuario_df.copy()
    for columna in columnas_a_normalizar:
        media = df_normalizado[columna].mean()
        desviacion_estandar = df_normalizado[columna].std()
        df_normalizado[columna] = (df_normalizado[columna] - media) / desviacion_estandar

    return df_normalizado

datos_acuario = {
    'temperatura': [25.0, 26.5, 24.8, 27.2, 25.9],
    'ph_agua': [7.2, 7.5, 7.0, 6.8, 7.3],
    'nivel_oxigeno': [8.5, 8.2, 9.0, 8.8, 8.6]
}

acuario_df = pd.DataFrame(datos_acuario)
acuario_normalizado = normalizar_z_score_acuario(acuario_df, ['temperatura', 'ph_agua'])
print(acuario_normalizado)
