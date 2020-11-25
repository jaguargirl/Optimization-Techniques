from tkinter import *
from searchEngine import *
from tkinter import messagebox
from utils import *


def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    if len(value) == 13:
        doc = str(value[10:12])
        doc += '.txt'
    else:
        doc = '0'
        doc += str(value[10:11])+'.txt'
    os.chdir("../bbc_sport")
    f = open(doc, "r")
    global det
    det.delete(1.0, 'end')
    det.insert(END, f.read())


def clear():
    global k, met, tol, request
    k.delete(0, 'end')
    request.delete(0, 'end')
    met.set('Cos')
    tol.set('0.85')


def printDocs(rel, out, mtol):
    a = 0
    b = 0
    c = 0
    docs = []
    for i in range(n):
        j = out[i]
        if rel[j] > mtol:
            doc = 'Document '+str(j+1)
            docs.append(doc)
            a += 1
        if rel[j] > (mtol/2):
            b += 1
        if rel[j] > 0.0:
            c += 1
    global listbox, precision, recall
    listbox.delete(0, 'end')
    for item in docs:
        listbox.insert(END, item)
    if b == 0 or c == 0:
        recTxt = ''
        prTxt = ''
        messagebox.showinfo('Warning', 'No relevant documents found')
    else:
        pr = a / c
        rec = a / b
        prTxt = 'Precision: ' + str(pr)
        recTxt = 'Recall: ' + str(rec)
    precision.set(prTxt)
    recall.set(recTxt)
    return a


def find():
    d = dictionary()
    m = len(d)
    global k, tol, met, request, resTxt
    try:
        mk = int(k.get())
    except ValueError:
        messagebox.showinfo('Warning', 'Please introduce truncated level')
        return
    mtol = float(tol.get())
    mrequest = request.get()
    if mrequest == '':
        messagebox.showinfo('Warning', 'Please write a request')
        return
    method = met.get()

    if mk >= 40:
        messagebox.showinfo('Warning', 'Truncated level should be lower than matrix rank (<40)')
        return
    Wi, Wk, df, dl = search_engine(n, mk)
    q = calcQ(d, mrequest, df, n)

    if method == 'Cos':
        cos, out, reTime = calcCos(q, Wi, Wk, n)
        nr = printDocs(cos, out, mtol)
    else:
        okapi, okapi_out, reTime = calcOkapi(q, df, dl, m, Wi, n)
        nr = printDocs(okapi, okapi_out, mtol)
    if nr != 0:
        txt = str(nr)+' results returned in '+str(reTime)
        resTxt.set(txt)
    # clear()


def create_window():
    win = Tk()
    win.title("Mini Search Engine")
    # main background
    Canvas(win, height=500, width=700, bg='#ccccff').pack()
    global k, met, tol, request, listbox, precision, recall, resTxt
    # Truncated level
    Label(win, text="Truncated level", fg="#6363f2", bg='#ccccff', bd=5).place(x=30, y=60)
    k = Entry(win, textvariable=StringVar())
    k.place(x=130, y=63)

    # Tolerance
    Label(win, text="Tolerance", bg='#ccccff', bd=5, fg="#6363f2").place(x=30, y=90)
    tol = StringVar()
    tol.set("0.85")
    tolVal = OptionMenu(win, tol, "0.85", "0.90", "0.95")
    tolVal.place(x=130, y=90)

    # Method
    Label(win, text="Method", bg='#ccccff', bd=5, fg="#6363f2").place(x=30, y=120)
    met = StringVar()
    met.set("Cos")
    method = OptionMenu(win, met, "Cos", "Okapi")
    method.place(x=130, y=120)

    # Request
    Label(win, text="Request", bg='#ccccff', bd=5, fg="#6363f2").place(x=330, y=60)
    request = Entry(win, textvariable=StringVar())
    request.place(x=400, y=65)
    Button(win, text="  Search  ", bd=5, command=find).place(x=550, y=60)

    # Statistics
    precision = StringVar()
    precision.set('')
    Label(win, textvariable=precision, bg='#ccccff', bd=5, fg="white").place(x=330, y=90)
    recall = StringVar()
    recall.set('')
    Label(win, textvariable=recall, bg='#ccccff', bd=5, fg="white").place(x=330, y=120)

    # Results details
    resTxt = StringVar()
    resTxt.set('')
    Label(win, textvariable=resTxt, bg='#ccccff', bd=5, fg="white").place(x=30, y=165)

    # Results
    listbox = Listbox(win)
    listbox.place(x=30, y=200)
    listbox.bind('<<ListboxSelect>>', onselect)
    scroller1 = Scrollbar(win)
    scroller1.place(x=154, y=201)
    scroller1.config(command=listbox.yview)
    listbox.config(yscrollcommand=scroller1.set)

    # Details
    global det
    det = Text(win, height=15, width=40)
    det.place(x=300, y=200)
    scroller = Scrollbar(win)
    scroller.place(x=625, y=201)
    scroller.config(command=det.yview)
    det.config(yscrollcommand=scroller.set)
    return win


def main():
    win = create_window()
    win.mainloop()


if __name__ == "__main__":
    k = 15
    tol = 0.9
    request = 'sport'
    listbox = ''
    n = 40
    met = 'Cos'
    det = 'Some details'
    resTxt = ''
    recall = ''
    precision = ''
    main()
