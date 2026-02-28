from sklearn.metrics import classification_report, confusion_matrix

def evaluar_modelo(df):

    reporte = classification_report(
        df["fraude_real"],
        df["fraude_predicho"]
    )

    matriz = confusion_matrix(
        df["fraude_real"],
        df["fraude_predicho"]
    )

    return {
        "Reporte de Clasificación": reporte,
        "Matriz de Confusión": matriz
    }