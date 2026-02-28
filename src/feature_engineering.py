import pandas as pd

def calcular_estadisticas_cliente(df):

    stats = df.groupby("id_cliente")["monto"].agg(["mean", "std"]).reset_index()
    stats.columns = ["id_cliente", "media_cliente", "desviacion_cliente"]

    df = df.merge(stats, on="id_cliente", how="left")

    return df


def agregar_z_score(df):

    df["z_score"] = (
        (df["monto"] - df["media_cliente"]) /
        df["desviacion_cliente"]
    )

    df["z_score"] = df["z_score"].fillna(0)

    return df


def agregar_flag_nocturno(df, hora_inicio_nocturna, hora_fin_nocturna):

    df["hora"] = df["fecha_hora"].dt.hour

    df["flag_nocturno"] = (
        df["hora"].between(hora_inicio_nocturna, hora_fin_nocturna)
    ).astype(int)

    return df


def agregar_flag_pais(df):

    df["flag_pais_distinto"] = (
        df["pais"] != df["pais_habitual"]
    ).astype(int)

    return df