## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.9.1) Updated in [27.02.2023]          ###

## ----------------------------------------------------##

# Bibliotecas necessárias para execução do código

import tkinter as tk
import oss, ss, report, setores, tiposmanut, pecas, relatoriospdf, funcionarios, equip, eqpcadastrados, viewss

# Variaveis de entrada

res2 = None
res = None
icon = "C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\enova.ico"

def main():
    main_menu = tk.Tk()
    main_menu.title("Menu-Cadastros")
    main_menu.geometry("240x640")
    main_menu.iconbitmap(default=icon)
    main_menu.config(bg='#202020')

    # Botões de acesso ás demais aplicações

    c_os = tk.Button(main_menu, text="Cadastro de O.S",
                     command=oss.cad_os, width=30)
    c_os.grid(row=1, column=1, padx=10, pady=10)

    c_ss = tk.Button(main_menu, text="Cadastro de S.S",
                     command=ss.cad_ss, width=30)
    c_ss.grid(row=2, column=1, padx=10, pady=10)

    c_eqp = tk.Button(
        main_menu, text="Cadastro de Equipamentos", command=equip.cad_eqp, width=30)
    c_eqp.grid(row=3, column=1, padx=10, pady=10)

    c_pcs = tk.Button(main_menu, text="Cadastro de Peças",
                      command=pecas.cad_pcs, width=30)
    c_pcs.grid(row=4, column=1, padx=10, pady=10)

    c_fun = tk.Button(
        main_menu, text="Cadastro de Funcionários", command=funcionarios.cad_fun, width=30)
    c_fun.grid(row=5, column=1, padx=10, pady=10)

    c_set = tk.Button(main_menu, text="Cadastro de Setores",
                      command=setores.cad_set, width=30)
    c_set.grid(row=6, column=1, padx=10, pady=10)

    c_set = tk.Button(main_menu, text="Tipos de Manutenção",
                      command=tiposmanut.cad_tip, width=30)
    c_set.grid(row=7, column=1, padx=10, pady=10)

    c_rep = tk.Button(main_menu, text="Reportar O.S's",
                      command=report.rep_os, width=30)
    c_rep.grid(row=8, column=1, padx=10, pady=10)

    c_relat = tk.Button(main_menu, text="Relatório de O.S's",
                      command=relatoriospdf.generate_report, width=30)
    c_relat.grid(row=9, column=1, padx=10, pady=10)

    c_eqv = tk.Button(main_menu, text="Equipamentos Cadastrados",
                      command=eqpcadastrados.cad_eqv, width=30)
    c_eqv.grid(row=10, column=1, padx=10, pady=10)

    v_ss = tk.Button(main_menu, text="SS's Cadastradas",
                      command=viewss.view_ss, width=30)
    v_ss.grid(row=11, column=1, padx=10, pady=10)

    # Função para fechar a interface

    def cancel_menu():
        main_menu.destroy()
        print()

    # Botão para fechar a interface

    c_left = tk.Button(main_menu, text="Sair", command=cancel_menu)
    c_left.grid(row=12, column=1, padx=10, pady=30)

    main_menu.mainloop()


if __name__ == "__main__":
    main()
