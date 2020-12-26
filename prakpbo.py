import tkinter

main_window = tkinter.Tk()

submit1 = tkinter.Button(main_window, text = "Tekan1")
submit2 = tkinter.Button(main_window, text = "Tekan2")

#method positioning
submit1.pack()
submit2.pack()

#method menampilkan GUI
main_window.mainloop()
