from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("600x250")
window.title("World Dictionary ")
entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

hausa_dict = {"come": "zo",
              "go": "je",
              "head": "kai",
              "leg": "kafa",
              "food": "adinci"
              }



def search(word):
    if word in hausa_dict:
        result.set(hausa_dict[word])
    
    else:
        result.set("Not found")
        print("Not found")

search_btn = Button(window, text="search", command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()
