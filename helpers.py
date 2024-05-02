from graph import create_graph
import math
import numpy as np
# В файле хранятся функции для вычисления значений программы
def calculate_r_i(x_left, x_right, z_left, z_right, m):
  return 0.5 * m * (x_right - x_left) - (z_right + z_left) / 2

def calculate_next_x(x_left, x_right, z_left, z_right, m):
  return 0.5 * (x_right + x_left) - (z_right - z_left) / (2 * m)

def calculate_function(x, sin_coef, sin_arg, cos_coef, cos_arg):
  return sin_coef * math.sin(sin_arg * x) + cos_coef * math.cos(cos_arg * x)

def calculate_m(r, M):
  result = 1
  if (M > 0):
    result = r * M
  return result

# arguments - массив x
# values - массив z
def calculate_M(arguments, values, t):
  M_array = []
  for i in range(1, t + 1):
    M_array.append(abs(values[i] - values[i - 1]) / (arguments[i] - arguments[i - 1]))
  return max(M_array)

def calculate_max_R(arguments, values, t, m):
  R_max = calculate_r_i(arguments[0], arguments[1], values[0], values[1], m)
  result = 1
  for i in range(1, t + 1):
    R = calculate_r_i(arguments[i - 1], arguments[i], values[i - 1], values[i], m)
    if (R > R_max):
      R_max = R
      result = i
  return result

def start_calculation(func_coef, borders, error, max_number_iter, mode, param, controls):
  x_array = np.array([borders[0], borders[1]])
  number_iteration = 2
  result = []
  print('Начало вычислений')
  # Высчитываем всё до конца
  # TODO: разобраться как пересчитывать значения для y_array, ибо сейчас это неверно
  if (mode == 'fixed'):
    # TODO: добавить условие на ошибку
    while (number_iteration < max_number_iter):
      x_array = np.sort(x_array)
      y_array = np.vectorize(calculate_function)(x_array, *func_coef)
      interval_index = calculate_max_R(x_array, y_array, number_iteration - 1, param)
      next_x = calculate_next_x(x_array[interval_index - 1], x_array[interval_index], y_array[interval_index - 1], y_array[interval_index], param)
      x_array = np.append(x_array, next_x)
      number_iteration += 1
      if x_array[interval_index] - x_array[interval_index - 1] < error or number_iteration == max_number_iter:
        result = [next_x, number_iteration, x_array]
        break
  else:
    # TODO: добавить условие на ошибку
    while (number_iteration < max_number_iter):
      x_array = np.sort(x_array)
      y_array = np.vectorize(calculate_function)(x_array, *func_coef)
      M_param = calculate_M(x_array, y_array, number_iteration - 1)
      m_param = calculate_m(param, M_param)
      interval_index = calculate_max_R(x_array, y_array, number_iteration - 1, m_param)
      next_x = calculate_next_x(x_array[interval_index - 1], x_array[interval_index], y_array[interval_index - 1], y_array[interval_index], m_param)
      x_array = np.append(x_array, next_x)
      number_iteration += 1
      if x_array[interval_index] - x_array[interval_index - 1] < error or number_iteration == max_number_iter:
        result = [next_x, number_iteration, x_array]
        break
  print(result)
  array_graph_points = np.linspace(borders[0], borders[1], 10000)
  y_array = np.full_like(x_array, np.min(np.vectorize(calculate_function)(x_array, *func_coef)) - 1)
  controls[0].set(str(calculate_function(result[0], *func_coef)))
  controls[1].set(str(result[0]))
  controls[2].set(str(result[1]))
  create_graph(array_graph_points, np.vectorize(calculate_function)(array_graph_points, *func_coef), x_array, y_array, next_x, calculate_function(next_x, *func_coef))
