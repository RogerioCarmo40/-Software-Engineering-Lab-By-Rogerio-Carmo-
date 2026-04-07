import tkinter as tk
from tkinter import simpledialog, messagebox
import math
import time


class TimerAnalogico:

    def __init__(self, root):
        self.root = root
        self.root.title("Timer Analógico")
        self.root.geometry("500x550")

        # Variáveis principais
        self.rodando = False
        self.tempo_inicio = None
        self.tempo_decorrido = 0
        self.intervalo_ciclo = None
        self.contagem = 0

        # Canvas para o relógio
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Texto contador
        self.label_contagem = tk.Label(
            root, text="Contagem: 0 pages", font=("Arial", 16))
        self.label_contagem.pack()

        # Botões
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Button(frame, text="Iniciar", width=10,
                  command=self.iniciar).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Pausar", width=10,
                  command=self.pausar).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Resetar", width=10,
                  command=self.resetar).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Salvar", width=10,
                  command=self.salvar).grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Sair", width=10, command=root.quit).grid(
            row=0, column=4, padx=5)

        self.desenhar_relogio()

    # ---------------------------------------------------
    # DESENHAR RELÓGIO BASE
    # ---------------------------------------------------

    def desenhar_relogio(self):

        self.canvas.delete("all")

        centro = 200
        raio = 180

        # círculo
        self.canvas.create_oval(
            centro-raio, centro-raio,
            centro+raio, centro+raio,
            width=3
        )

        # marcações
        for i in range(60):

            angulo = math.radians(i * 6)

            x1 = centro + (raio-10) * math.sin(angulo)
            y1 = centro - (raio-10) * math.cos(angulo)

            x2 = centro + raio * math.sin(angulo)
            y2 = centro - raio * math.cos(angulo)

            largura = 3 if i % 5 == 0 else 1

            self.canvas.create_line(x1, y1, x2, y2, width=largura)

    # ---------------------------------------------------
    # DESENHAR PONTEIRO
    # ---------------------------------------------------

    def desenhar_ponteiro(self):

        self.canvas.delete("ponteiro")

        centro = 200
        raio = 150

        segundos = self.tempo_decorrido % 60

        angulo = math.radians(segundos * 6)

        x = centro + raio * math.sin(angulo)
        y = centro - raio * math.cos(angulo)

        self.canvas.create_line(
            centro, centro,
            x, y,
            width=4,
            fill="red",
            tag="ponteiro"
        )

    # ---------------------------------------------------
    # ATUALIZAÇÃO DO TIMER
    # ---------------------------------------------------

    def atualizar(self):

        if self.rodando:

            agora = time.time()
            self.tempo_decorrido = int(agora - self.tempo_inicio)

            # verificar ciclos
            if self.intervalo_ciclo > 0:
                nova_contagem = self.tempo_decorrido // self.intervalo_ciclo

                if nova_contagem != self.contagem:
                    self.contagem = nova_contagem
                    self.label_contagem.config(
                        text=f"Contagem: {self.contagem} pages"
                    )

            self.desenhar_ponteiro()

        self.root.after(1000, self.atualizar)

    # ---------------------------------------------------
    # INICIAR
    # ---------------------------------------------------

    def iniciar(self):

        if self.intervalo_ciclo is None:

            valor = simpledialog.askinteger(
                "Intervalo",
                "Digite o intervalo em segundos:"
            )

            if not valor or valor <= 0:
                return

            self.intervalo_ciclo = valor

        if not self.rodando:

            self.tempo_inicio = time.time() - self.tempo_decorrido
            self.rodando = True
            self.atualizar()

    # ---------------------------------------------------
    # PAUSAR
    # ---------------------------------------------------

    def pausar(self):

        if self.rodando:

            self.rodando = False

    # ---------------------------------------------------
    # RESETAR
    # ---------------------------------------------------

    def resetar(self):

        self.rodando = False
        self.tempo_decorrido = 0
        self.contagem = 0

        self.label_contagem.config(text="Contagem: 0 pages")

        self.desenhar_relogio()
        self.desenhar_ponteiro()

    # ---------------------------------------------------
    # SALVAR
    # ---------------------------------------------------

    def salvar(self):

        segundos = self.tempo_decorrido
        minutos = segundos // 60
        horas = segundos // 3600

        texto = (
            f"Timer: {segundos} segundos\n"
            f"{minutos} minutos\n"
            f"{horas} horas\n"
            f"Contagem: {self.contagem} pages"
        )

        with open("sessao_timer.txt", "w", encoding="utf-8") as f:
            f.write(texto)

        messagebox.showinfo("Salvo", "Arquivo sessao_timer.txt criado!")

# ---------------------------------------------------
# EXECUÇÃO
# ---------------------------------------------------


if __name__ == "__main__":

    root_it = tk.Tk()

    app = TimerAnalogico(root_it)

    root_it.mainloop()
