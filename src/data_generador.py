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



    