"""import pandas as pd 
import numpy as np 
from config import*
from datetime import timedelta, datetime
rand.seed(semilla_alearoria)

def generar_clients(cantidad_clientes):
  
    return pd.DataFrame({

        'id_cliente': np.arange(cantidad_clientes),

        'pais_habitual': rand.choice(['BR','AR','CL'], size=cantidad_clientes)

    })


def generar_transacciones(clientes):
    
    lista_transacciones=[]

    for _,fila in clientes.iterrows():

        media_monto = rand.uniform(20,200)
        desviacion_monto = media_monto*0.3

        for _ in range (transaccion_por_cliente):

            fecha = datetime(2024,1,1) + timedelta(
                minutes= rand.randint(0,60*24*30) )

            es_fraude = rand.rand() < proporcion_fraude

            if es_fraude:
                monto= rand.uniform(media_monto*6, media_monto*4)
                pais= rand.choice(["US", "MX", "CO"])
            else:
                monto= rand.normal(media_monto, desviacion_monto)
                pais= fila['pais_habitual']

            lista_transacciones.append({
                "id_cliente": fila["id_cliente"],
                "fecha_hora": fecha,
                "monto": max(1, monto),
                "pais": pais,
                "es_fraude_real": int(es_fraude)
            })

    return pd.DataFrame(lista_transacciones)
"""

import pandas as pd
import numpy as np
import random
from config import cantidad_transacciones

def generar_clientes(cantidad_clientes):

    paises = ["Argentina", "Brasil", "Chile", "Uruguay"]

    clientes = pd.DataFrame({
        "id_cliente": range(1, cantidad_clientes + 1),
        "pais_habitual": np.random.choice(paises, cantidad_clientes),
        "media_monto_base": np.random.uniform(1000, 5000, cantidad_clientes)
    })

    return clientes


def generar_transacciones(clientes):

    transacciones = []

    paises = ["Argentina", "Brasil", "Chile", "Uruguay"]

    for _ in range(cantidad_transacciones):

        cliente = clientes.sample(1).iloc[0]

        monto = np.random.normal(cliente["media_monto_base"], 500)

        # 5% fraude artificial
        es_fraude = np.random.rand() < 0.05

        if es_fraude:
            monto *= 4  # monto exagerado

        pais_transaccion = random.choice(paises)

        fecha_hora = pd.Timestamp.now() - pd.Timedelta(
            minutes=np.random.randint(0, 60*24*30)
        )

        transacciones.append([
            cliente["id_cliente"],
            abs(monto),
            pais_transaccion,
            fecha_hora,
            int(es_fraude)
        ])

    df = pd.DataFrame(
        transacciones,
        columns=[
            "id_cliente",
            "monto",
            "pais",
            "fecha_hora",
            "fraude_real"
        ]
    )

    # 🔥 Merge correcto con datos del cliente
    df = df.merge(
        clientes[["id_cliente", "pais_habitual"]],
        on="id_cliente",
        how="left"
    )

    return df



    