import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# TODO: Добавить возможность отображения точек внизу и на графике отображения min
def create_graph(x, y):
  plt.plot(x, y)
  plt.xlabel('X')
  plt.ylabel('F(x)')
  plt.title('График функции')
  plt.grid(True)
  plt.show()

  # # Вставка графика в интерфейс Tkinter
  # fig = plt.gcf()
  # canvas = FigureCanvasTkAgg(fig, master=window)
  # canvas.draw()
  # canvas.get_tk_widget().pack()