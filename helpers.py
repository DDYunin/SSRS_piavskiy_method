from graph import create_graph

# В файле хранятся функции для вычисления значений программы
def calculate_r_i(x_left, x_right, z_left, z_right, m):
  return 0.5 * m * (x_right - x_left) - (z_right + z_left) / 2

def calculate_next_x(x_left, x_right, z_left, z_right, m):
  return 0.5 * (x_right + x_left) - (z_right - z_left) / (2 * m)

def calculate_m(r, M):
  result = 1
  if (M > 0):
    result = r * M
  return result

# arguments - массив x
# values - массив z
def calculate_M(arguments, values, t):
  M = 0
  for i in range(1, t + 1):
    M = max(M, abs(values[i] - values[i - 1]) / (arguments[i] - arguments[i - 1]))
  return M

def start_calculation():
  print('Начало')
  create_graph()