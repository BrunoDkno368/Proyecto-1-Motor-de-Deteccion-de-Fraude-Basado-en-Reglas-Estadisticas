"""from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

def evaluar_modelo(df):
    '''
    Calcula metricas de desempeño del sistema de deteccion
    '''
    y_real= df['es_fraude_real']
    y_predicho= df['fraude_predicho']

    resultados= {
        'matriz_confusion': confusion_matrix(y_real, y_predicho),
        'precision': precision_score(y_real, y_predicho),
        'recall': recall_score(y_real, y_predicho),
        'f1_score': f1_score(y_real, y_predicho)
        
        }
        
    return resultados
    """

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