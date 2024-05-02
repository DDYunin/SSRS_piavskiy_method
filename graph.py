import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# TODO: Добавить возможность отображения точек внизу и на графике отображения min
def create_graph(x, y, x_points, y_points, x_min, y_min):
  plt.plot(x, y)
  plt.scatter(x_points, y_points, color='red', label='Точки на оси x', alpha=0.15)
  plt.scatter(x_min, y_min, color='green', s=10)
  plt.xlabel('X')
  plt.ylabel('F(x)')
  plt.title('График функции')
  plt.grid(True)
  plt.legend()
  plt.show()