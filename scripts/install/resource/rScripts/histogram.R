#script que permite hacer el manejo de datos desde un archivo csv para generar un histograma con
#la informacion que presente dicho archivo, exporta la imagen a formato svg para
#obtener una mayor calidad de la imagen...
#entradas: input.csv - title graphic - name image - path output.
#salidad: imagen svg con el histograma

#recibimos los valores de los argumentos
args <- commandArgs(TRUE);
nameCSV = args[1];
nameSVG = args[2];
titleData = args[3];

#incluimos las librerias...
library("ggplot2");

#formamos la imagen SVG
svg(nameSVG);

#hacemos la lectura del archivo csv...
dataCSV = read.csv(nameCSV, header=TRUE, sep=",");

#obtenemos el range bind...
rangeBind = (abs(min(dataCSV)) + abs(max(dataCSV)))/20;

data = ggplot(dataCSV, aes(x=dataInfo)) +

  geom_histogram(Bindcolor="white",fill="black") +

  labs(x = "Values Element", y="Frequency", title=titleData)

  data + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
  panel.background = element_blank(), axis.line = element_line(colour = "black"))


dev.off();
