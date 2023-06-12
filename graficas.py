import matplotlib.pyplot as plt

def grafica_linea(x,y):
    fig, ax = plt.subplots(figsize=(16,8))
    
    ax.plot(x,y)
    ax.plot(x,y, 'o')
    plt.xticks(x, rotation=90)
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.25)
    plt.grid(True)
    plt.title("Máximo número de contagios por estado")
    ax.set_xlabel("Estado")
    ax.set_ylabel("Contagios")
    
    for x, y in zip(x, y):
        ax.text(x, y, f"{y}", fontsize=8, rotation=40)
        
    plt.show()
    
    
    

def grafica_barra(x,y):
    fig, ax = plt.subplots(figsize=(16,8))
    
    ax.bar(x,y, color='blue')
    plt.xticks(x, rotation=90)
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.25)
    plt.grid(False)
    plt.title("Percentaje de contagios respecto a la población")
    ax.set_xlabel("")
    ax.set_ylabel("Porcentaje")
    
    def add_value_labels(ax, spacing=5):
        """Add labels to the end of each bar in a bar chart.

        Arguments:
            ax (matplotlib.axes.Axes): The matplotlib object containing the axes
                of the plot to annotate.
            spacing (int): The distance between the labels and the bars.
        """

        # labels
        for rect in ax.patches:
            # Get X and Y placement of label from rect.
            y_value = rect.get_height()
            x_value = rect.get_x() + rect.get_width() / 2

            # Number of points between bar and label. Change to your liking.
            space = spacing
            # Vertical alignment for positive values
            va = 'bottom'

            # If value of bar is negative: Place label below bar
            if y_value < 0:
                # Invert space to place label below
                space *= -1
                # Vertically align label at top
                va = 'top'

            # Use Y value as label and format number with one decimal place
            label = "{:.1f}%".format(y_value)

            # Create annotation
            ax.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center', 
                fontsize=6,
                color='red',
                rotation=0,# Horizontally center label
                va=va)                      # Vertically align label differently for
                                        # positive and negative values.


    # Call the function above. All the magic happens there.
    add_value_labels(ax)
    plt.show()
    
    
def grafica_linea2(x,y, label):
    fig, ax = plt.subplots(figsize=(16,8))
    
    ax.plot(x,y)
    ax.plot(x,y, 'o')
    plt.xticks(x, rotation=90)
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.25)
    plt.grid(True)
    plt.title("Serie de tiempo mensual "+ label)
    ax.set_xlabel("Mes")
    ax.set_ylabel("Contagios")
    
    for x, y in zip(x, y):
        ax.text(x, y, f"{y}", fontsize=8, rotation=40)
        
    plt.show()