import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ta Te Ti")
        self.turno = "X"  # El primer turno es del jugador X
        self.tablero = [" " for _ in range(9)]  # Defiune 9 espacios vacíos
        self.botones = []  # Almacena las referencias a los botones
        self.crear_tablero()
        self.turno_label = tk.Label(self.root, text=f"Turno del jugador: {self.turno}", font=('Arial', 18), bg="lightblue")
        self.turno_label.grid(row=3, column=0, columnspan=3, sticky="nsew")
    
    def crear_tablero(self):
        # Crea el tablero principal del juego, de 3x3 y 9 espacios vacios
        for i in range(9):
            boton = tk.Button(self.root, text=" ", font=('Arial', 32, 'bold'), width=5, height=2, 
                              bg="white", fg="black", relief="raised", bd=10,
                              command=lambda i=i: self.al_hacer_click(i))
            boton.grid(row=i // 3, column=i % 3, padx=5, pady=5)  # establece el padding (o disctancia) entre los botones
            self.botones.append(boton)
    
    def al_hacer_click(self, indice):
        # Verifica si la casilla se encuentra ocupada
        if self.tablero[indice] == " ":
            self.tablero[indice] = self.turno
            self.botones[indice].config(text=self.turno, fg="red" if self.turno == "X" else "blue", disabledforeground="black", state="disabled")
            if self.verificar_ganador():
                self.mostrar_ganador(self.turno)
            elif " " not in self.tablero:  # Verifica si hay un empate
                self.mostrar_ganador("Empate")
            else:
                self.turno = "O" if self.turno == "X" else "X"  # Cambia de turno
                self.actualizar_turno()
    
    def verificar_ganador(self):
        # Define todas las combinaciones que ganen 
        combinaciones_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontales
                                   (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticales
                                   (0, 4, 8), (2, 4, 6)]  # Diagonales
        
        for a, b, c in combinaciones_ganadoras:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] and self.tablero[a] != " ":
                # Cambia el color del boton que haya ganado
                self.botones[a].config(bg="lightgreen")
                self.botones[b].config(bg="lightgreen")
                self.botones[c].config(bg="lightgreen")
                return True
        return False
    
    def mostrar_ganador(self, ganador):
        if ganador == "Empate":
            messagebox.showinfo("Resultado", "¡Es un empate!")
        else:
            messagebox.showinfo("Resultado", f"¡El jugador {ganador} ha ganado!")
        self.reiniciar_tablero()
    
    def reiniciar_tablero(self):
        self.tablero = [" " for _ in range(9)]
        for boton in self.botones:
            boton.config(text=" ", state="normal", bg="white")
        self.turno = "X"
        self.actualizar_turno()

    def actualizar_turno(self):
        # Actualiza el texto del turno en la etiqueta
        self.turno_label.config(text=f"Turno del jugador: {self.turno}", fg="red" if self.turno == "X" else "blue")

# Se crea la ventana del juego
root = tk.Tk()
root.configure(bg="lightblue")  # color del background
juego = TicTacToe(root)
root.mainloop()
