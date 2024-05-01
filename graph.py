import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_graph():
  x = [1, 2, 3, 4, 5]
  y = [2, 3, 5, 1, 11]
  plt.plot(x, y)
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('График')
  plt.grid(True)
  plt.show()

  # # Вставка графика в интерфейс Tkinter
  # fig = plt.gcf()
  # canvas = FigureCanvasTkAgg(fig, master=window)
  # canvas.draw()
  # canvas.get_tk_widget().pack()