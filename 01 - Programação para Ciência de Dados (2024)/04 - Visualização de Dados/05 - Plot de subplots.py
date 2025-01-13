import matplotlib.pyplot as plt
import numpy as np

graph1Data = np.arange(2000, 2011)
graph2Data = np.arange(2000, 2011)
graph3Data = np.arange(2000, 2011)

graph1Labels = np.arange(0, 11)

figure = plt.figure(figsize=(9, 6))

spec = figure.add_gridspec(nrows=4, ncols=2)

graph1 = figure.add_subplot(spec[0:2, 0:2])
graph2 = figure.add_subplot(spec[3:4, 0:1])
graph3 = figure.add_subplot(spec[3:4, 1:2])


graph1.plot(graph1Data, graph1Labels, 'ro--')
graph1.set_title('Titulo Graph1')
graph1.set_xlabel('Ano')
graph1.set_ylabel('Quantidade')

graph2.plot(graph2Data)

graph3.plot(graph3Data)

plt.show()
