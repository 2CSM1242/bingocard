import random
import tkinter as tk
import numpy as np

root = tk.Tk()
root.title("BINGOカード")
root.geometry("800x600")

label = tk.Label(text="", font=("Book Antiqua", 20))
label.place(x=0, y=0)


shikibetsu =[]
bingocard = np.zeros((5, 5), dtype=int)

def button(b, i, j):
    b.config(bg="gray30")
    bingocard[i][j] = 0
    check_bingo()

def check_bingo():  # ビンゴとリーチのチェック
    bingo = False
    reach = False

def check_bingo():  # ビンゴとリーチのチェック
    bingo = False
    reach = False

    # 行でビンゴとリーチをチェック
    for row in bingocard:
        zero_count = np.sum(row == 0)  # 行内の0の数を数える
        if zero_count == 5:
            bingo = True
        elif zero_count == 4:
            reach = True

    # 列でビンゴとリーチをチェック
    for col in range(5):
        zero_count = np.sum(bingocard[:, col] == 0)  # 列内の0の数を数える
        if zero_count == 5:
            bingo = True
        elif zero_count == 4:
            reach = True

    # 左上から右下の対角線でビンゴとリーチをチェック
    zero_count = np.sum(np.diag(bingocard) == 0)
    if zero_count == 5:
        bingo = True
    elif zero_count == 4:
        reach = True

    # 右上から左下の対角線でビンゴとリーチをチェック
    zero_count = np.sum(np.diag(np.fliplr(bingocard)) == 0)
    if zero_count == 5:
        bingo = True
    elif zero_count == 4:
        reach = True

    # 判定結果の出力
    if bingo:
        label.config(text="BINGO!")  # ビンゴの場合
    elif reach:
        label.config(text="リーチ!")  # リーチの場合
    else:
        label.config(text="")  # まだビンゴではない場合

def generate(): #カードの出力
    n = 1
    y = 20

    for i in range(5):
        numberlist = []
        w = 135
        j = 0
        while len(numberlist) < 5:
            if i == 2 and len(numberlist) == 2:
                number = 0
                numberlist.append(number)
                bango = tk.Button(root, text="Free", bg="gray85", font=("Book Antiqua", 40)) #リストの中の数字を表示
                bango.config(command=lambda b=bango, x=i, y=len(numberlist)-1: button(b, x, y))
                bango.place(x=w, y=y, width=105, height=110)
                w += 105
                

            number = random.randint(n, n+14)
            if number not in numberlist:
                numberlist.append(number)  #リストの中に生成した数字を入れる
                bango = tk.Button(root, text=number, bg="gray85", font=("Book Antiqua", 40)) #リストの中の数字を表示
                bango.config(command=lambda b=bango, x=i, y=len(numberlist)-1: button(b, x, y))
                bango.place(x=w, y=y, width=105, height=110)
                w += 105

        bingocard[i] = numberlist
        n += 15
        y += 110
        
                
    h = hash(str(bingocard))
    
    if h not in shikibetsu:
        shikibetsu.append(h)
    else:
        generate()
    
    

def newcard(): #新しいカードを出力する
    cancel = tk.Button(root, text="new", font=("Book Antiqua", 30), command=lambda: (generate()))
    cancel.place(x=680, y=510)
    bingocard = np.zeros((5, 5), dtype=int)
    check_bingo()

def generate_card():
    generate_card = tk.Button(root, text="ビンゴカードを一枚取る", font=("Book Antiqua", 40),command=lambda: (generate(), generate_card.destroy(), newcard()))
    generate_card.place(x=100, y=230)

generate_card()


root.mainloop()

print(bingocard)
