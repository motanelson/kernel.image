import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

class RamDiskBuilderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RAM Disk TXT Builder")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Memória onde os ficheiros são ligados
        self.memory_buffer = ""
        self.loaded_files = []

        # Barra superior com botões
        top = tk.Frame(root, bg="black")
        top.pack(fill="x", pady=5)

        btn_style = {
            "bg": "white",
            "fg": "black",
            "activebackground": "#dddddd",
            "activeforeground": "black",
            "relief": "flat",
            "width": 10
        }

        tk.Button(top, text="OPEN", command=self.open_files, **btn_style).pack(side="left", padx=5)
        tk.Button(top, text="SAVE", command=self.save_file, **btn_style).pack(side="left", padx=5)
        tk.Button(top, text="CLEAR", command=self.clear_memory, **btn_style).pack(side="left", padx=5)

        # Área de texto (preview/debug)
        self.text = ScrolledText(
            root,
            bg="black",
            fg="white",
            insertbackground="white",
            font=("Consolas", 10)
        )
        self.text.pack(fill="both", expand=True, padx=5, pady=5)

        self.log("RAM Disk TXT Builder iniciado.\n")

    def log(self, msg):
        self.text.insert("end", msg)
        self.text.see("end")

    def open_files(self):
        paths = filedialog.askopenfilenames(
            title="Abrir ficheiros TXT",
            filetypes=[("Text files", "*.txt"), ("All files", "*")]
        )

        if not paths:
            return

        for path in paths:
            try:
                paths=path.split("/")
                with open(path, "r") as f:
                    
                    data = str(f.read())

                # Liga ficheiros em memória (estilo ramdisk)
                self.memory_buffer =self.memory_buffer +  "|"+paths[len(paths)-1]+"|" + data
                self.loaded_files.append(path)
                data = data + "|"
                self.log(f"[OK] Carregado: {path} ({len(data)} bytes)\n")
            except Exception as e:
                self.log(f"[ERRO] {path}: {e}\n")

        self.log(f"Memória total: {len(self.memory_buffer)} bytes\n\n")

    def save_file(self):
        if not self.memory_buffer:
            messagebox.showwarning("Aviso", "Nenhum ficheiro carregado.")
            return

        path = filedialog.asksaveasfilename(
            title="Guardar RAM Disk",
            defaultextension=".img",
            filetypes=[("RAM Disk Image", "*.img"), ("All files", "*")]
        )

        if not path:
            return

        try:
            with open(path, "w") as f:
                f.write(self.memory_buffer)

            self.log(f"[OK] Gravado: {path} ({len(self.memory_buffer)} bytes)\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def clear_memory(self):
        self.memory_buffer=""
        self.loaded_files.clear()
        self.text.delete("1.0", "end")
        self.log("Memória limpa.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = RamDiskBuilderGUI(root)
    root.mainloop()

