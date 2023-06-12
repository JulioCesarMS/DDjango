import matplotlib.pyplot as plt

def muestra_tabla(datos):
    column_labels = ['Estado', 'Fecha', 'Máximo']
    fig, ax = plt.subplots(figsize=(16,8))
    ax.table(cellText=datos, colLabels=column_labels,loc="center")
    ax.axis('tight')
    ax.axis('off')
    plt.show()
    
    
    
def muestra_tabla2(datos):
    column_labels = ['Estado', 'Población', '# Contagios', 'Porcentaje']
    fig, ax = plt.subplots(figsize=(16,8))
    ax.table(cellText=datos, colLabels=column_labels,loc="center")
    ax.axis('tight')
    ax.axis('off')
    plt.show()