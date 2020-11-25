from tkinter import *
import time as t
import numpy as np
import os
from collections import Counter
from numpy.linalg import norm


dictionary = ["sport", "tennis", "gold", "champion", "record", "doping", "race", "Olympic", "football", "win", "lose", "athlete",
     "medals", "transfer", "world", "teams", "victory", "rules", "coach", "former", "performed", "championship",
     "athletics", "club", "qualification", "national", "international", "awards", "success", "season"]
m = len(dictionary)


def search_engine(k):
    A = np.zeros((m, n))
    files = []
    directory = "../bbc_sport"
    j = 0
    df = np.zeros(m)
    for file in os.listdir(directory):
        files.append(file)
        filepath = os.path.join(directory, file)
        f = open(filepath, 'r')
        wordcount = Counter(f.read().split())
        for i in range(m):
            nr = wordcount[dictionary[i]]
            if nr != 0:
                df[i] += 1
            A[i, j] = nr
        f.close()
        j += 1
    W = np.zeros((m, n))  # weights matrix
    for i in range(m):
        idf = np.log(n / df[i])
        for j in range(n):
            tf = A[i][j] / max(A[i, :])
            W[i][j] = tf * idf

    U, s, Vt = np.linalg.svd(W)
    S = np.diag(s)
    r = np.linalg.matrix_rank(W)

    uk = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            uk[i, j] = U[i, j]

    sk = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            sk[i, j] = S[i, j]

    x, y = Vt.shape
    vk = np.zeros((k, x))
    for i in range(k):
        for j in range(x):
            vk[i, j] = Vt[i, j]

    Wk = np.dot(np.dot(uk, sk), vk)
    return W, Wk, df


def find():
    global k
    mk = int(k.get())
    global tol
    mtol = float(tol.get())
    global request
    mrequest = request.get()
    W, Wk, df = search_engine(mk)
    q = np.zeros((m, 1))
    words = mrequest.split()
    nrr = np.zeros((m, 1))

    for i in range(len(words)):
        for j in range(len(dictionary)):
            if words[i] == dictionary[j]:
                nrr[j] += 1
    for i in range(len(words)):
        for j in range(len(dictionary)):
            if words[i] == dictionary[j]:
                wordcount = Counter(words)
                nr = wordcount[dictionary[j]]
                idf = np.log(n / df[j])
                tf = nr / max(nrr[j])
                q[j] = tf * idf
    cos = np.zeros((n, 1))

    t0 = t.perf_counter()
    for i in range(n):
        cos[i] = np.dot(q.T, Wk[:, i]) / norm(q) * norm(W[:, i])
    t1 = t.perf_counter()
    out = np.argsort(-1 * cos, axis=0)[:n]
    print("Returned in ", str(t1 - t0))
    a = 0
    b = 0
    c = 0
    docs = []
    for i in range(n):
        j = out[i]
        if cos[j] > mtol:
            doc = 'Document '+str(j)
            print(doc)
            docs.append(doc)
            a += 1
        if cos[j] > 0.5:
            b += 1
        if cos[j] > 0:
            c += 1
    global listbox
    for item in docs:
        listbox.insert(END, item)
    precision = a / c
    print("Precision: ", precision)
    recall = a / b
    print("Recall: ", recall)


def create_window():
    win = Tk()
    win.title("Mini Search Engine")
    # main background
    Canvas(win, height=600, width=700, bg='#ccccff').pack()
    # Matrix rank label
    Label(win, text='Matrix rank = 40', fg="white", bg='#ccccff', bd=5).place(x=30, y=30)
    # Truncated level
    Label(win, text="Truncated level", fg="#6363f2", bg='#ccccff', bd=5).place(x=30, y=60)
    global k
    k = Entry(win, textvariable=StringVar())
    k.place(x=150, y=63)
    Label(win, text="<r", bg='#ccccff', bd=5, fg="#6363f2").place(x=250, y=60)
    # Tolerance
    Label(win, text="Tolerance", bg='#ccccff', bd=5, fg="#6363f2").place(x=30, y=105)
    global tol
    tol = StringVar()
    tol.set("0.85")
    tolVal = OptionMenu(win, tol, "0.85", "0.90", "0.95")
    tolVal.place(x=150, y=105)
    # Request
    Label(win, text="Request", font="Arial", width=10, bg='#ccccff', bd=5, fg="#6363f2").place(x=330, y=50)
    global request
    request = Entry(win, textvariable=StringVar())
    request.place(x=430, y=55)
    Button(win, text="  Search  ", bd=5, command=find).place(x=580, y=51)
    global listbox
    listbox = Listbox(win)
    listbox.place(x=30, y=160)
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
    main()
