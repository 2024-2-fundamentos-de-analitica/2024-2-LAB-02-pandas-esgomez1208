"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    tb0 = 'files/input/tbl0.tsv'
    df = pd.read_csv(tb0, sep='\t')

    # Se agrupa en base a c1, y se le aplica solo a c2
    medias = df.groupby('c1')['c2'].mean()
    medias.name = 'c2'
    
    return medias
