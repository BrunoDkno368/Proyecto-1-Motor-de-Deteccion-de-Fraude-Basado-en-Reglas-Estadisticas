
def calcular_score_riesgo(df, umbral_z):

    df["score_riesgo"] = 0

    df.loc[df["z_score"] > umbral_z, "score_riesgo"] += 50
    df.loc[df["flag_nocturno"] == 1, "score_riesgo"] += 20
    df.loc[df["flag_pais_distinto"] == 1, "score_riesgo"] += 30

    return df


def clasificar_transacciones(df):

    df["fraude_predicho"] = (df["score_riesgo"] >= 70).astype(int)

    return df