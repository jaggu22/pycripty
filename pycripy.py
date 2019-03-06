import tkinter as tk

def getCoding():
	chars=['a', 'e', 'i', 'o', 'u', 'y', '.', ',', 's', 't', 'd', 'n', 'g', 'l', 'r', ';', 'h', 'E', 'A', 'I', 'H', 'S', 'T', 'Y', 'W', 'O', 'U', 'b', 'c', 'f', 'j', 'k', 'm', 'p', 'q', 'v', 'w', 'x', 'z', ':', '&', '"', "'", '!', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '[', ']', '{', '}', 'B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'V', 'X', 'Z', '+', '-', '*', '/', '=', '<', '>', '%', '#', '\\', '`', '@', '$', '^', '|', '~']
	with open('code.csv','r') as code:
		data=code.read().strip().split('\n')
		codes={}
		decodes={}
		count=0
		for code in data:
			codes[chars[count]]=code
			decodes[code]=chars[count]
			count+=1
	return(codes,decodes)

codes,decodes=getCoding()
def encript(txtE):
	txt='.'.join([codes.get(x,x) for x in txtE.get(1.0,tk.END).strip()])
	txtE.delete(1.0,tk.END)
	txtE.insert(1.0,txt)
def decript(txtE):
	txt=''.join([decodes.get(x,x) for x in txtE.get(1.0,tk.END).strip().split('.')])
	txtE.delete(1.0,tk.END)
	txtE.insert(1.0,txt)

win=tk.Tk()

menuBar=tk.Menu(win)
menuBar.add_command(label="Encript",command=lambda :encript(txtE))
menuBar.add_command(label="Decript",command=lambda :decript(txtE))
win.config(menu=menuBar)

txtE=tk.Text(win)
txtE.pack()


tk.mainloop()
