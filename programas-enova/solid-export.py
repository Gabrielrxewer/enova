<<<<<<< HEAD
import os
import tkinter as tk
import tkinter.filedialog as fd
import win32com.client

def select_files():
    filetypes = (("SolidWorks files", "*.sldprt;*.sldasm"), ("All files", "*.*"))
    filenames = fd.askopenfilenames(title="Selecione os arquivos", filetypes=filetypes)
    export_files(filenames)

def export_files(filenames):
    swApp = win32com.client.Dispatch("SldWorks.Application")
    swApp.Visible = True
    for filename in filenames:
        try:
            swModel = swApp.OpenDoc(filename, 1)
            swModelDocExt = swModel.Extension
            swModelDocExt.SaveAs(os.path.splitext(filename)[0] + ".dxf", 0, 0, None, 0, 0)
            swCustomInfo = swModel.CustomInfo2("")
            for i in range(swCustomInfo.Count):
                if swCustomInfo.Item(i)[0] == "Chapa Metálica":
                    swCustomInfo.Item(i)[1] = "Sim"
                    break
        except Exception as e:
            print(f"Erro ao exportar o arquivo {filename}: {e}")
        finally:
            swApp.CloseDoc(filename)

root = tk.Tk()
select_button = tk.Button(root, text="Selecionar Arquivos", command=select_files)
select_button.pack()
root.mainloop()
=======
import os
import tkinter as tk
import tkinter.filedialog as fd
import win32com.client

def select_files():
    filetypes = (("SolidWorks files", "*.sldprt;*.sldasm"), ("All files", "*.*"))
    filenames = fd.askopenfilenames(title="Selecione os arquivos", filetypes=filetypes)
    export_files(filenames)

def export_files(filenames):
    swApp = win32com.client.Dispatch("SldWorks.Application")
    swApp.Visible = True
    for filename in filenames:
        try:
            swModel = swApp.OpenDoc(filename, 1)
            swModelDocExt = swModel.Extension
            swModelDocExt.SaveAs(os.path.splitext(filename)[0] + ".dxf", 0, 0, None, 0, 0)
            swCustomInfo = swModel.CustomInfo2("")
            for i in range(swCustomInfo.Count):
                if swCustomInfo.Item(i)[0] == "Chapa Metálica":
                    swCustomInfo.Item(i)[1] = "Sim"
                    break
        except Exception as e:
            print(f"Erro ao exportar o arquivo {filename}: {e}")
        finally:
            swApp.CloseDoc(filename)

root = tk.Tk()
select_button = tk.Button(root, text="Selecionar Arquivos", command=select_files)
select_button.pack()
root.mainloop()
>>>>>>> 523eec05995f79699c2366f9c29ad68a318f295c
