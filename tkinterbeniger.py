import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import random as rd
import json
import os

ALFABETO = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ",
            "o","p","q","r","s","t","u","v","w","x","y","z"]

# ─── Lógica central ──────────────────────────────────────────────────────────

def crear_array_mensaje(mensaje):
    arr = []
    for c in mensaje.lower():
        if c in ALFABETO:
            arr.append([ALFABETO.index(c)])
    return np.array(arr)

def matriz_aleatoria(n):
    det = 0
    while det == 0:
        m = np.array([[rd.randint(1, 10) for _ in range(n)] for _ in range(n)])
        det = np.linalg.det(m)
    return m

def encriptar_mensaje(mensaje):
    arr = crear_array_mensaje(mensaje)
    n = len(arr)
    if n == 0:
        raise ValueError("El mensaje no contiene caracteres válidos.")
    enc = matriz_aleatoria(n)
    clave = enc @ arr
    return enc, clave

def desencriptar_mensaje(encriptador_arr, clave_arr):
    inv = np.linalg.inv(encriptador_arr)
    resultado = np.round(inv @ clave_arr).astype(int)
    msg = ""
    for fila in resultado:
        for idx in fila:
            if 0 <= idx < len(ALFABETO):
                msg += ALFABETO[idx]
    return msg

# ─── Aplicación ──────────────────────────────────────────────────────────────

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Encriptador Matricial")
        self.resizable(False, False)
        self._build_ui()
        self._center()

    def _center(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"+{(sw-w)//2}+{(sh-h)//2}")

    def _build_ui(self):
        PAD = dict(padx=16, pady=8)

        # Título
        tk.Label(self, text="Encriptador Matricial", font=("Courier", 16, "bold"),
                 fg="#3ce0f9", bg="#0e1a2b").pack(fill="x", ipady=14)
        self.configure(bg="#0e1a2b")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=14, pady=(8, 14))

        # Estilo
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#0e1a2b", borderwidth=0)
        style.configure("TNotebook.Tab", background="#132a56", foreground="#aac4e0",
                        font=("Courier", 10), padding=[12, 6])
        style.map("TNotebook.Tab", background=[("selected","#1f3d72")],
                  foreground=[("selected","#3ce0f9")])
        style.configure("TFrame", background="#0e1a2b")

        # ── Pestaña encriptar ──────────────────────────────────────────────
        tab_enc = ttk.Frame(notebook)
        notebook.add(tab_enc, text="  Encriptar  ")
        self._build_enc_tab(tab_enc)

        # ── Pestaña desencriptar ───────────────────────────────────────────
        tab_dec = ttk.Frame(notebook)
        notebook.add(tab_dec, text="  Desencriptar  ")
        self._build_dec_tab(tab_dec)

    # ── Helpers de widgets ────────────────────────────────────────────────────

    def _label(self, parent, text):
        return tk.Label(parent, text=text, font=("Courier", 9),
                        fg="#7aadcc", bg="#0e1a2b", anchor="w")

    def _entry(self, parent, width=50):
        e = tk.Entry(parent, width=width, font=("Courier", 11),
                     bg="#132a56", fg="#e8f4fd", insertbackground="#3ce0f9",
                     relief="flat", bd=4)
        return e

    def _textbox(self, parent, height=4, width=50):
        t = tk.Text(parent, height=height, width=width, font=("Courier", 10),
                    bg="#132a56", fg="#e8f4fd", insertbackground="#3ce0f9",
                    relief="flat", bd=4, state="disabled",
                    wrap="word")
        return t

    def _btn(self, parent, text, cmd, accent=False):
        bg = "#3ce0f9" if accent else "#1f3d72"
        fg = "#0e1a2b" if accent else "#b0d4ea"
        b = tk.Button(parent, text=text, command=cmd,
                      font=("Courier", 10, "bold"), bg=bg, fg=fg,
                      activebackground="#5aeaff", activeforeground="#0e1a2b",
                      relief="flat", bd=0, padx=14, pady=6, cursor="hand2")
        return b

    def _set_text(self, widget, text):
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("end", text)
        widget.configure(state="disabled")

    # ── Pestaña encriptar ─────────────────────────────────────────────────────

    def _build_enc_tab(self, parent):
        P = dict(padx=16, pady=4)

        self._label(parent, "Mensaje a encriptar:").pack(fill="x", **P)
        self.enc_input = self._entry(parent, 52)
        self.enc_input.pack(fill="x", **P)

        # Botones
        fr_btn = tk.Frame(parent, bg="#0e1a2b")
        fr_btn.pack(fill="x", **P)
        self._btn(fr_btn, "⟳  Encriptar", self._do_encrypt, accent=True).pack(side="left", padx=(0,8))
        self._btn(fr_btn, "↓  Guardar archivos", self._save_enc).pack(side="left")

        self._label(parent, "Clave pública (vector resultado):").pack(fill="x", **P)
        self.enc_out_clave = self._textbox(parent, height=4)
        self.enc_out_clave.pack(fill="x", **P)

        self._label(parent, "Matriz encriptadora:").pack(fill="x", **P)
        self.enc_out_mat = self._textbox(parent, height=6)
        self.enc_out_mat.pack(fill="x", **P)

        self._label(parent, "Estado:").pack(fill="x", **P)
        self.enc_status = self._textbox(parent, height=2)
        self.enc_status.pack(fill="x", **P)

        # Almacén temporal
        self._enc_data = None

    def _do_encrypt(self):
        msg = self.enc_input.get().strip()
        if not msg:
            messagebox.showwarning("Aviso", "Escribe un mensaje primero.")
            return
        try:
            enc, clave = encriptar_mensaje(msg)
            self._enc_data = {"encriptador": enc, "clave": clave}

            self._set_text(self.enc_out_clave, str(clave.tolist()))
            self._set_text(self.enc_out_mat, str(enc.tolist()))
            self._set_text(self.enc_status, f"✓  Mensaje encriptado ({len(enc)}×{len(enc)} matriz)")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _save_enc(self):
        if not self._enc_data:
            messagebox.showwarning("Aviso", "Encripta un mensaje primero.")
            return

        carpeta = filedialog.askdirectory(title="Selecciona carpeta de destino")
        if not carpeta:
            return

        ruta_enc  = os.path.join(carpeta, "encryptador.json")
        ruta_clave = os.path.join(carpeta, "clavePublica.json")

        with open(ruta_enc, "w") as f:
            json.dump({"encryptador": self._enc_data["encriptador"].tolist()}, f, indent=2)
        with open(ruta_clave, "w") as f:
            json.dump({"clavePublica": self._enc_data["clave"].tolist()}, f, indent=2)

        self._set_text(self.enc_status, f"✓  Archivos guardados en:\n   {carpeta}")

    # ── Pestaña desencriptar ──────────────────────────────────────────────────

    def _build_dec_tab(self, parent):
        P = dict(padx=16, pady=4)

        # Clave pública
        fr1 = tk.Frame(parent, bg="#0e1a2b")
        fr1.pack(fill="x", **P)
        self._label(fr1, "Archivo clave pública (clavePublica.json):").pack(side="left")
        self._btn(fr1, "Examinar", self._browse_clave).pack(side="right")

        self.dec_clave_path = self._entry(parent, 52)
        self.dec_clave_path.pack(fill="x", **P)

        # Encriptador
        fr2 = tk.Frame(parent, bg="#0e1a2b")
        fr2.pack(fill="x", **P)
        self._label(fr2, "Archivo encriptador (encryptador.json):").pack(side="left")
        self._btn(fr2, "Examinar", self._browse_enc).pack(side="right")

        self.dec_enc_path = self._entry(parent, 52)
        self.dec_enc_path.pack(fill="x", **P)

        fr_btn = tk.Frame(parent, bg="#0e1a2b")
        fr_btn.pack(fill="x", **P)
        self._btn(fr_btn, "⟳  Desencriptar", self._do_decrypt, accent=True).pack(side="left")

        self._label(parent, "Mensaje descifrado:").pack(fill="x", **P)
        self.dec_out = self._textbox(parent, height=4)
        self.dec_out.pack(fill="x", **P)

        self._label(parent, "Estado:").pack(fill="x", **P)
        self.dec_status = self._textbox(parent, height=2)
        self.dec_status.pack(fill="x", **P)

    def _browse_clave(self):
        path = filedialog.askopenfilename(
            title="Selecciona clavePublica.json",
            filetypes=[("JSON", "*.json"), ("Todos", "*.*")]
        )
        if path:
            self.dec_clave_path.delete(0, "end")
            self.dec_clave_path.insert(0, path)

    def _browse_enc(self):
        path = filedialog.askopenfilename(
            title="Selecciona encryptador.json",
            filetypes=[("JSON", "*.json"), ("Todos", "*.*")]
        )
        if path:
            self.dec_enc_path.delete(0, "end")
            self.dec_enc_path.insert(0, path)

    def _do_decrypt(self):
        clave_path = self.dec_clave_path.get().strip()
        enc_path   = self.dec_enc_path.get().strip()

        if not clave_path or not enc_path:
            messagebox.showwarning("Aviso", "Selecciona ambos archivos.")
            return
        try:
            with open(clave_path) as f:
                clave_arr = np.array(json.load(f)["clavePublica"])
            with open(enc_path) as f:
                enc_arr = np.array(json.load(f)["encryptador"])

            msg = desencriptar_mensaje(enc_arr, clave_arr)
            self._set_text(self.dec_out, msg)
            self._set_text(self.dec_status, "✓  Mensaje descifrado correctamente")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Archivo no encontrado:\n{e}")
        except KeyError as e:
            messagebox.showerror("Error", f"Clave faltante en JSON: {e}")
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "La matriz encriptadora no tiene inversa.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = App()
    app.mainloop()