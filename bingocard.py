import random
import tkinter as tk

root = tk.Tk()
root.title("BINGOカード")
root.geometry("800x600")

shikibetsu =[]


def button(b):
    b.config(bg="gray30")

def generate(): #カードの出力
    bingocard = []
    def number_row(n, h):    #hには配置したい場所のy座標を入力
        numberlist = []
        w = 135
        if n == 31: #Freeマスのある列の処理
            while len(numberlist) < 5:
                if len(numberlist) == 2:    #Freeマスの処理
                    bango = tk.Button(root, text="Free", bg="gray30", font=("Book Antiqua", 40)) #リストの中の数字を表示
                    bango.place(x=w, y=h, width=105, height=110)
                    w += 105
                    numberlist.append(0)
                else:

                    number = random.randint(n, n+14)   #n~n+14までの数字をランダムに生成
                    if number not in numberlist:   #出た数字が重複していないとき
                        numberlist.append(number)  #リストの中に生成した数字を入れる
                        bango = tk.Button(root, text=number, bg="gray85", font=("Book Antiqua", 40)) #リストの中の数字を表示
                        bango.config(command=lambda b=bango: button(b))
                        bango.place(x=w, y=h, width=105, height=110)
                        w += 105

                        bingocard.append(number)
        else:
            while len(numberlist) < 5:
                number = random.randint(n, n+14)   #n~mまでの数字をランダムに生成
                if number not in numberlist:   #出た数字が重複していないとき
                    numberlist.append(number)  #リストの中に生成した数字を入れる
                    bango = tk.Button(root, text=number, bg="gray85", font=("Book Antiqua", 40)) #リストの中の数字を表示
                    bango.config(command=lambda b=bango: button(b))
                    bango.place(x=w, y=h, width=105, height=110)
                    w += 105

                    bingocard.append(number)
    number_row(1, 20)
    number_row(16, 130)
    number_row(31, 240)
    number_row(46, 350)
    number_row(61, 460)
    h = hash(str(bingocard))
    
    if h not in shikibetsu:
        shikibetsu.append(h)
    else:
        generate()
    

def newcard(): #新しいカードを出力する
    cancel = tk.Button(root, text="new", font=("Book Antiqua", 30), command=lambda: (generate()))
    cancel.place(x=680, y=510)
def generate_card():
    generate_card = tk.Button(root, text="ビンゴカードを一枚取る", font=("Book Antiqua", 40),command=lambda: (generate(), generate_card.destroy(), newcard()))
    generate_card.place(x=100, y=230)

generate_card()


root.mainloop()


