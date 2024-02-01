import tkinter as tk

def verificar():
  if len(operando_1_text.get()) == 0 or len(operando_2_text.get()) == 0:
    print("Tanto Operando 1 como Operando 2 deben ser ingresados.")
  else:
    realizarOperacion()

def realizarOperacion():
  global operador
  global operacionesAnteriores
  if len(operando_3_text.get()) == 0:
    if (operando_1_text.get().isnumeric()
        and operando_2_text.get().isnumeric()):
      operador += str(int(operando_1_text.get()) + int(operando_2_text.get()))
    else:
      operador += operando_1_text.get() + operando_2_text.get()
  else:
    if (operando_1_text.get().isnumeric()
        and operando_2_text.get().isnumeric()
        and operando_3_text.get().isnumeric()):
      operador += str(
          int(operando_1_text.get()) + int(operando_2_text.get()) +
          int(operando_3_text.get()))
    else:
      operador += operando_1_text.get() + operando_2_text.get(
      ) + operando_3_text.get()

    if operador in operacionesAnteriores:
      resultado_text.set(operador)
      usuarioAnterior_text.set(operacionesAnteriores[operador])
    else:
      operacionesAnteriores[operador] = usuario_text.get()
      usuarioAnterior_text.set(usuario_text.get())
      resultado_text.set(operador)

    clear()

def clear():
  global operador
  operador = ""


window = tk.Tk()
window.title("Calculadora")
window.geometry("392x900")
#Text variables.
usuario_text = tk.StringVar()
operando_1_text = tk.StringVar()
operando_2_text = tk.StringVar()
operando_3_text = tk.StringVar()
usuarioAnterior_text = tk.StringVar()
resultado_text = tk.StringVar()

operador = ""
operacionesAnteriores = {}

#Usuario - Label + Input
usuario_label = tk.Label(text="Usuario").place(x=10, y=40)

usuario = tk.Entry(window,
                   textvariable=usuario_text,
                   font=("Arial", 20, "bold"),
                   width=18,
                   borderwidth=10,
                   justify="center").place(x=10, y=60)

#Operando 1 - Label + Input
operando_1_label = tk.Label(text="Operando 1").place(x=10, y=120)

operando_1 = tk.Entry(window,
                      textvariable=operando_1_text,
                      font=("Arial", 20, "bold"),
                      width=18,
                      borderwidth=10,
                      justify="center").place(x=10, y=140)

#Operando 2 - Label + Input
operando_2_label = tk.Label(text="Operando 2").place(x=10, y=200)

operando_2 = tk.Entry(window,
                      textvariable=operando_2_text,
                      font=("Arial", 20, "bold"),
                      width=18,
                      borderwidth=10,
                      justify="center").place(x=10, y=220)

#Operando 3 - Label + Input
operando_3_label = tk.Label(text="Operando 3").place(x=10, y=280)

operando_3 = tk.Entry(window,
                      textvariable=operando_3_text,
                      font=("Arial", 20, "bold"),
                      width=18,
                      borderwidth=10,
                      justify="center").place(x=10, y=300)

#Boton - Realizar operacion
boton = tk.Button(text="Realizar operacion",
                  command=lambda: verificar()).place(x=125, y=380)

#Resultado - (Label + Input (UsuarioAnterior)) + (Label + Input (Resultado))
usuarioAnterior_label = tk.Label(
    text="Usuario que realizo la operacion").place(x=10, y=440)

usuarioAnterior = tk.Entry(window,
                           font=("Arial", 20, "bold"),
                           width=18,
                           borderwidth=10,
                           justify="center",
                           textvariable=usuarioAnterior_text).place(x=10,
                                                                    y=460)

resultado_label = tk.Label(text="Resultado").place(x=10, y=520)

resultado = tk.Entry(window,
                     font=("Arial", 20, "bold"),
                     width=18,
                     borderwidth=10,
                     justify="center",
                     textvariable=resultado_text).place(x=10, y=540)

tk.mainloop()
