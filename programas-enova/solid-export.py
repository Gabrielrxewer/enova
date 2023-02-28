import os
import tkinter as tk
import tkinter.filedialog as fd
import win32com.client


class SolidWorksExporter:
    def __init__(self):
        self.swApp = None
        self.assembly = None
        self.selections = None
        self.directory = None
        self.export_options = None
        self.dxf_exporter = None

    def select_assembly(self):
        """Abre uma janela de seleção de arquivo e abre a montagem selecionada no SolidWorks."""
        filename = fd.askopenfilename(title="Selecione a montagem", filetypes=[("Arquivo de montagem", "*.sldasm")])
        if filename:
            self.swApp = win32com.client.Dispatch("SldWorks.Application")
            self.swApp.Visible = True
            self.assembly = self.swApp.OpenDoc6(filename, 2, 2, "", 0, 0)

    def export_as_dxf(self):
        """Exporta todas as peças da montagem selecionada como arquivos DXF."""
        self.selections = self.assembly.GetComponents(True)
        self.export_options = self.swApp.GetExportFileData(1)
        self.export_options.SetFileType(3)  # DXF file type
        if "Chapa metálica" in self.export_options.GetProperties():
            self.export_options.SetPropertyValue("Chapa metálica", True)  # Seleciona a opção "Chapa metálica"
        for selection in self.selections:
            component = selection.GetModelDoc2()
            name = component.GetTitle()
            dxf_filename = os.path.join(self.directory, name + ".dxf")
            self.dxf_exporter = component.Extension.GetExportFileData(3)  # DXF export data
            self.dxf_exporter.SetFileName(dxf_filename)
            self.dxf_exporter.SetExportFileData(self.export_options)
            component.Extension.SaveAs(dxf_filename, 0)  # Save as DXF file

    def select_directory(self):
        """Abre uma janela de seleção de diretório e define o diretório de saída para os arquivos DXF."""
        self.directory = fd.askdirectory(title="Selecione o diretório de saída")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.exporter = SolidWorksExporter()
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Exportador SolidWorks")
        self.create_widgets()

    def create_widgets(self):
        self.select_assembly_button = tk.Button(self.master, text="Selecionar Montagem", command=self.exporter.select_assembly)
        self.select_assembly_button.pack(pady=20)

        self.export_button = tk.Button(self.master, text="Exportar como DXF", command=self.exporter.export_as_dxf)
        self.export_button.pack()

        self.select_directory_button = tk.Button(self.master, text="Selecionar Diretório", command=self.exporter.select_directory)
        self.select_directory_button.pack(pady=20)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
