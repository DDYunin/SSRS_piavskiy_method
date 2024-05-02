import tkinter as tk
# Мои модули
from helpers import calculate_r_i, calculate_next_x, calculate_m, calculate_M, start_calculation
from graph import create_graph

window = tk.Tk()
window.title("Поиск глобального минимума методом Пиявского")
window.geometry("900x500")

# Создание первого фрейма и размещение его с помощью grid
frame_params = tk.Frame(window, bg="lightgray")
frame_params.grid(row=0, column=0, sticky="nsew")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

title = tk.Label(frame_params, text="Поиск глобального минимума функции F(x)", bg="lightgray", font=("Arial", 14))
title.pack(pady=10)

func_frame = tk.Frame(frame_params, height=50)
func_frame.pack()

func_label = tk.Label(func_frame, text='F(x) =', font=("Arial", 12), bg="lightgray")
coef_sin = tk.Entry(func_frame, width=5, justify="right", font=("Arial", 12, 'bold'))
sin_label = tk.Label(func_frame, text='Sin', font=("Arial", 12), bg="lightgray")
argument_sin = tk.Entry(func_frame, width=5, justify="right", font=("Arial", 12, 'bold'))
argument_label_sin = tk.Label(func_frame, text='X +', font=("Arial", 12), bg="lightgray")
coef_cos = tk.Entry(func_frame, width=5, justify="right", font=("Arial", 12, 'bold'))
cos_label = tk.Label(func_frame, text='Cos', font=("Arial", 12), bg="lightgray")
argument_cos = tk.Entry(func_frame, width=5, justify="right", font=("Arial", 12, 'bold'))
argument_label_cos = tk.Label(func_frame, text='X', font=("Arial", 12), bg="lightgray")

for index, item in enumerate([func_label, coef_sin, sin_label, argument_sin, argument_label_sin, coef_cos, cos_label, argument_cos, argument_label_cos]):
  item.grid(row=0, column=index)

# Задание интервала
range_frame = tk.Frame(frame_params)
range_frame.pack(pady=10)

range_first_label = tk.Label(range_frame, text='X \u2208 { ', font=("Arial", 12), bg="lightgray")
range_left_border = tk.Entry(range_frame, width=5, justify="right", font=("Arial", 12, 'bold'))
range_second_label = tk.Label(range_frame, text=' ; ', font=("Arial", 12), bg="lightgray")
range_right_border = tk.Entry(range_frame, width=5, justify="right", font=("Arial", 12, 'bold'))
range_third_label = tk.Label(range_frame, text=' } ', font=("Arial", 12), bg="lightgray")

for index, item in enumerate([range_first_label, range_left_border, range_second_label, range_right_border, range_third_label]):
  item.grid(row=0, column=index)

# Создание переменной StringVar для хранения выбранной опции
option = tk.StringVar(value='fixed')
radio_frame = tk.Frame(frame_params, bg="lightgray")
radio_frame.pack()

def toggle_entry_state():
  if option.get() == 'fixed':
    input_param_r.config(state="disabled")
    input_param_m.config(state="normal")
  else:
    input_param_r.config(state="normal")
    input_param_m.config(state="disabled")

radio_button = tk.Radiobutton(radio_frame, text="Фиксированное значение параметра m", variable=option, value='fixed', bg="lightgray", command=toggle_entry_state)
radio_button.pack(anchor='w')
radio_button1 = tk.Radiobutton(radio_frame, text="Адаптивное значение параметра m", variable=option, value='responsive', bg="lightgray", command=toggle_entry_state)
radio_button1.pack(anchor='w')

# Дополнительные параметры
extra_params_frame = tk.Frame(frame_params, bg="lightgray")
extra_params_frame.pack(anchor='center', pady=10)

label_param_r = tk.Label(extra_params_frame, text='Параметр метода r: ', font=("Arial", 12), bg="lightgray")
label_param_m = tk.Label(extra_params_frame, text='Параметр метода m: ', font=("Arial", 12), bg="lightgray")
label_param_error = tk.Label(extra_params_frame, text='Допустимая погрешность: ', font=("Arial", 12), bg="lightgray")
label_param_number_iter = tk.Label(extra_params_frame, text='Максимальное число итераций: ', font=("Arial", 12), bg="lightgray")

input_param_r = tk.Entry(extra_params_frame, font=("Arial", 12, 'bold'), justify="right", state='disabled')
input_param_m = tk.Entry(extra_params_frame, font=("Arial", 12, 'bold'), justify="right")
input_param_error = tk.Entry(extra_params_frame, font=("Arial", 12, 'bold'), justify="right")
input_param_number_iter = tk.Entry(extra_params_frame, font=("Arial", 12, 'bold'), justify="right")


extra_params_array = [
  [label_param_r, input_param_r],
  [label_param_m, input_param_m],
  [label_param_error, input_param_error],
  [label_param_number_iter, input_param_number_iter]
]
for row in range(len(extra_params_array)):
  for column in range(len(extra_params_array[row])):
    extra_params_array[row][column].grid(row=row, column=column, sticky='w')

calculate_button = tk.Button(frame_params, text='Рассчитать', command=lambda: start_calculation(*prepare_params()))
calculate_button.pack(pady=15)

# Вывод результатов
result_frame = tk.Frame(frame_params, bg="lightgray")
result_frame.pack(anchor='center', pady=10)

result_lbl_y = tk.Label(result_frame, text='Найденный минимум: ', font=("Arial", 12), bg="lightgray")
result_lbl_x = tk.Label(result_frame, text='Найденная координата: ', font=("Arial", 12), bg="lightgray")
result_lbl_number = tk.Label(result_frame, text='Число проведенных операций ', font=("Arial", 12), bg="lightgray")

entry_var_y = tk.StringVar(value="")
entry_var_x = tk.StringVar(value="")
entry_var_number = tk.StringVar(value="")

result_input_y = tk.Entry(result_frame, font=("Arial", 12, 'bold'), justify="right", state='readonly', textvariable=entry_var_y)
result_input_x = tk.Entry(result_frame, font=("Arial", 12, 'bold'), justify="right", state='readonly', textvariable=entry_var_x)
result_input_number = tk.Entry(result_frame, font=("Arial", 12, 'bold'), justify="right", state='readonly', textvariable=entry_var_number)


result_array = [
  [result_lbl_y, result_input_y],
  [result_lbl_x, result_input_x],
  [result_lbl_number, result_input_number],
]
for row in range(len(result_array)):
  for column in range(len(result_array[row])):
    result_array[row][column].grid(row=row, column=column, sticky='w')

def prepare_params():
  func_coef = [
    float(coef_sin.get()),
    float(argument_sin.get()),
    float(coef_cos.get()),
    float(argument_cos.get())
  ]
  borders = [
    float(range_left_border.get()),
    float(range_right_border.get())
  ]
  error = float(input_param_error.get())
  max_iteration = float(input_param_number_iter.get())
  mode = option.get()
  param = None
  if (mode == 'fixed'):
    param = float(input_param_m.get())
  else:
    param = float(input_param_r.get())
  controls = [
    entry_var_y,
    entry_var_x,
    entry_var_number
  ]
  print([func_coef, borders, error, max_iteration, mode, param, controls])
  return [func_coef, borders, error, max_iteration, mode, param, controls]

window.mainloop()