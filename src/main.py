"""import pandas as pd 
from config import*
from data_generador import generar_clients, generar_transacciones
from evaluacion import evaluar_modelo
from feature_engineering import calcular_estadisticas_cliente, agregar_z_score, agregar_flag_nocturno, agregar_flag_pais
from motor_scoring import calcular_score_riesgo, clasificar_transacciones

def main():
    clientes= generar_clients(cantidad_clientes)
    df= generar_transacciones(clientes)

    df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])

    df= calcular_estadisticas_cliente(df)
    df=agregar_z_score(df)
    
    df=agregar_flag_nocturno(df,hora_inicio_nocturna, hora_fin_nocturna)
    df=agregar_flag_pais(df)

    df=calcular_score_riesgo(df,umbral_z)
    df=clasificar_transacciones(df)

    metricas= evaluar_modelo(df)

    print("\n === RESULTADOS DEL SISTEMA DE DETECCION=== \n")
    for clave, valor in metricas.items():
        print(f"{clave}:")
        print(valor)
        print()

if __name__ == "__main__":
   main()  
"""

import pandas as pd
import os
from datetime import datetime

from config import *
from data_generador import generar_clientes, generar_transacciones
from feature_engineering import (
    calcular_estadisticas_cliente,
    agregar_z_score,
    agregar_flag_nocturno,
    agregar_flag_pais
)
from motor_scoring import calcular_score_riesgo, clasificar_transacciones
from evaluacion import evaluar_modelo


def main():

    print("\n=== INICIANDO MOTOR DE DETECCIÓN DE FRAUDE ===\n")

    # -----------------------
    # 1. Generación de datos
    # -----------------------
    clientes = generar_clientes(cantidad_clientes)
    df = generar_transacciones(clientes)

    df["fecha_hora"] = pd.to_datetime(df["fecha_hora"])

    # -----------------------
    # 2. Feature Engineering
    # -----------------------
    df = calcular_estadisticas_cliente(df)
    df = agregar_z_score(df)
    df = agregar_flag_nocturno(df, hora_inicio_nocturna, hora_fin_nocturna)
    df = agregar_flag_pais(df)

    # -----------------------
    # 3. Scoring
    # -----------------------
    df = calcular_score_riesgo(df, umbral_z)
    df = clasificar_transacciones(df)

    # -----------------------
    # 4. Evaluación
    # -----------------------
    metricas = evaluar_modelo(df)

    print("\n=== RESULTADOS DEL SISTEMA DE DETECCIÓN ===\n")
    for clave, valor in metricas.items():
        print(clave)
        print(valor)
        print()

    # -----------------------
    # 5. Exportación Auditable
    # -----------------------

    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Exportar dataset completo con scoring
    ruta_csv = f"outputs/transacciones_scored_{timestamp}.csv"
    df.to_csv(ruta_csv, index=False)

    # Exportar métricas
    ruta_metricas = f"outputs/metricas_{timestamp}.txt"
    with open(ruta_metricas, "w", encoding="utf-8") as f:
        for clave, valor in metricas.items():
            f.write(f"{clave}\n")
            f.write(str(valor))
            f.write("\n\n")

    print("=== EXPORTACIÓN COMPLETADA ===")
    print(f"Dataset guardado en: {ruta_csv}")
    print(f"Métricas guardadas en: {ruta_metricas}")
    print("\n=== FIN DE EJECUCIÓN ===\n")


if __name__ == "__main__":
    main()