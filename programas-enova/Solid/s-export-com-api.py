import os
import tkinter as tk
from tkinter import filedialog
import SolidWorks.Interop.sldworks as sw
import SolidWorks.Interop.swconst as swconst

def export_to_dxf(filepath, export_sheet_metal=False):
    swApp = sw.SldWorks()
    swApp.Visible = True
    swModel = swApp.OpenDoc(filepath, swconst.swDocumentTypes_e.swDocPART)
    swModelExt = swModel.Extension
    swExportData = swModelExt.GetExportFileData(swconst.swExportDataFileType_e.swExportDataFileType_DXF)
    if export_sheet_metal:
        swExportData.SetSheets(swconst.swDXFExportSheetMetalOption_e.swDXFExportSheetMetal)
    swModelExt.SaveAs(os.path.splitext(filepath)[0] + ".dxf", 0, 0, swExportData, 0, 0)

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        export_sheet_metal = var_export_sheet_metal.get()
        export_to_dxf(file_path, export_sheet_metal)

# Create GUI
root = tk.Tk()
root.title("Export to DXF")

# Create widgets
btn_select_file = tk.Button(root, text="Select File", command=select_file)
btn_cancel = tk.Button(root, text="Cancel", command=root.quit)
var_export_sheet_metal = tk.BooleanVar()
chk_export_sheet_metal = tk.Checkbutton(root, text="Export as Sheet Metal", variable=var_export_sheet_metal)

# Layout widgets
btn_select_file.pack(pady=10)
chk_export_sheet_metal.pack(pady=10)
btn_cancel.pack(pady=10)

# Run GUI
root.mainloop()
