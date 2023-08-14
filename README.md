# TP1-TC-Grupo3
Se trabajó con el código base de la PlotToolG2 correspondiente al repositorio https://github.com/Teoria-de-Circuitos-II/PlotTool-G2.git
## Mejoras agregadas:
### Botón "Hide / Show line" 
Se agregó la posibilidad de esconder una línea seleccionada con el botón "Hide / Show line" y volver a mostrarla, para no tener que eliminar la línea
cada vez que se desea no verla, con el fin de realizar comparaciones. Para esconder una línea ya ploteada basta con seleccionarla en la lista de líneas
y presionar el botón "Hide / Show line", el mismo proceso debe hacerse para volver a mostrar una línea escondida previamente.

### Modificación de Layout de la app
Con fines de organizar las opciones existentes para modificar los gráficos según su funcionalidad, se agruparon las mismas en las secciones "Info", "Axis", "View" y "Cursors",
para encontrar más rápida y organizadamente la opción que se requiera

#### Sección "Info"
Contiene las opciones que permiten modificar el nombre de la línea y la pestaña donde se dibuja.

#### Sección "Axis"
Contiene todas las opciones relacionadas a la modificación de datos con los que interactúan los ejes (escala, offset y selección del canal que representa el eje).

#### Sección "View"
Contiene todas las opciones que modifican cómo se representan las líneas en los gráficos, como color, estilo de línea y representación de puntos y las opciones de 
reducción del ruido en la señal representada.

#### Sección "Cursors"
Permite mostrar y esconder hasta dos cursores que pueden ser usados en cualquiera de las líneas representadas. Para modificar la posición de cualquiera de los cursores,
debe seleccionarse el cursor a mover desde la sección "cursors" y la línea a la que se lo quiere asociar. Una vez seleccionado el cursor y la línea, basta con hacer click 
en cualquier parte del gráfico para que el cursor se posicione en el punto representado más cercano a la zona clickeada.

### Tabla de información

En adición a la sección de cursores, se agregó una tabla que contiene los datos relevantes que pueden obtenerse a partir de la posición de los cursores colocados sobre una misma señal,
ya que además de mostrar las coordenadas del gráfico donde se encuentran los mismos, se representan los valores "Y2-Y1", "X2-X1", "1/(X2-X1)" y "Slope", que pueden ser útiles dependiendo
la medición que se pretenda realizar, pudiendo tratarse a "Y2-Y1" como la amplitud de una señal en particular, "X2-X1" como el período, y su inversa como la frecuencia de la misma. 
El valor "Slope" representa la pendiente de la línea recta que une las coordenadas de los dos cursores posicionados, que podría ser útil en el caso de necesitar medir la velocidad de
crecimiento de una línea.
