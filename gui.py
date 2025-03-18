#- * -coding: utf - 8 - * -
from TrainingSetsUtil import get_words
from TrainingSetsUtil import spam_training_set
from TrainingSetsUtil import ham_training_set
from tkinter import *

##main
window = Tk()
window.title("Spam Filter")
window.configure(background = "white")



# c is an experimentally obtained value
def classify(message, training_set, prior = 0.5, c = 3.7e-4):
    msg_terms = get_words(message)
    msg_probability = 1

    for term in msg_terms:
    	if term in training_set:
        	msg_probability *= training_set[term]
    	else :
        	msg_probability *= c

    return msg_probability * prior

# uncomment this to provide input to the program


## 0.2 and 0.8 because the ratio of samples for spam and ham were the 0.2 - 0.8

## clickfunction
def click():
    entered_text = textentry.get()
    #print("Entered text is: "+entered_text)
    spam_probability = classify(entered_text, spam_training_set, 0.2)
    ham_probability = classify(entered_text, ham_training_set, 0.8)
    if spam_probability > ham_probability:
        output.delete(0.0, END)
        output.insert(END, 'Your mail has been classified as SPAM.')
    else:
        output.delete(0.0, END)
        output.insert(END, 'Your mail has been classified as HAM.')

def close_window():
    window.destroy()
    exit()

## photo
photo1 = PhotoImage(file = "logo.gif")
Label(window, image = photo1, bg = "white").grid(row = 0, column = 0, sticky = W)


## label
Label(window, text = "Enter the mail you would like to test:", bg = "white", fg = "black", font = "none 12 bold").grid(row = 1, column = 0, sticky = W)

## text entry box
textentry = Entry(window, width = 100, bg = "white", fg = "black")
textentry.grid(row = 2, column = 0, sticky = W)
#height=10, wrap=WORD, 

## submit button
Button(window, text = "SUBMIT", width = 6, command = click).grid(row = 3, column = 0, sticky = W)

Label(window, text = "\nResult:", bg = "white", fg = "black", font = "none 12 bold").grid(row = 4, column = 0, sticky = W)

output = Text(window, width = 75, height = 6, wrap = WORD, background = "white", fg = "black")
output.grid(row = 5, column = 0, columnspan = 2, sticky = W)

Button(window, text = "Exit", width = 14, command = close_window).grid(row = 6, column = 0, sticky = W)

window.mainloop()