from graph import create_graph
import math
# В файле хранятся функции для вычисления значений программы
def calculate_r_i(x_left, x_right, z_left, z_right, m):
  return 0.5 * m * (x_right - x_left) - (z_right + z_left) / 2

def calculate_next_x(x_left, x_right, z_left, z_right, m):
  return 0.5 * (x_right + x_left) - (z_right - z_left) / (2 * m)

def calculate_function(sin_coef, sin_arg, cos_coef, cos_arg, x):
  return sin_coef * math.sin(sin_arg * x) + cos_coef * math.cos(cos_arg * x)

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

def calculate_max_R(arguments, values, t, m):
  R_max = calculate_r_i(arguments[0], arguments[1], values[0], values[1], m)
  result = 1
  for i in range(1, t + 1):
    R = calculate_r_i(arguments[i - 1], arguments[i], values[i - 1], values[i], m)
    if (R > R_max):
      R_max = R
      result = i
  return result

def start_calculation(func_coef, borders, error, max_number_iter, mode, param):
  x_array = []
  y_array = []
  number_iteration = 0
  print('Начало вычислений')
  # Высчитаем левую границу интервала
  number_iteration += 1
  x_array.append(borders[0])
  y_array.append(calculate_function(*func_coef, borders[0]))
  # Высчитываем правую границу интервала
  number_iteration += 1
  x_array.append(borders[1])
  y_array.append(calculate_function(*func_coef, borders[1]))
  # Высчитываем всё до конца
  # TODO: разобраться как пересчитывать значения для y_array, ибо сейчас это неверно
  if (mode == 'fixed'):
    # TODO: добавить условие на ошибку
    while (number_iteration <= max_number_iter):
      x_array.sort()
      interval_index = calculate_max_R(x_array, y_array, number_iteration - 1, param)
      next_x = calculate_next_x(x_array[interval_index - 1], x_array[interval_index], y_array[interval_index - 1], y_array[interval_index], param)
      x_array.append(next_x)
      y_array.append(calculate_function(*func_coef, next_x))
      number_iteration += 1
  else:
    # TODO: добавить условие на ошибку
    while (number_iteration <= max_number_iter):
      x_array.sort()
      M_param = calculate_M(x_array, y_array, number_iteration - 1)
      m_param = calculate_m(param, M_param)
      interval_index = calculate_max_R(x_array, y_array, number_iteration - 1, m_param)
      next_x = calculate_next_x(x_array[interval_index - 1], x_array[interval_index], y_array[interval_index - 1], y_array[interval_index], m_param)
      x_array.append(next_x)
      y_array.append(calculate_function(*func_coef, next_x))
      number_iteration += 1
  # create_graph()

def fixed_calculation():
  pass

def responsive_calculation():
  pass