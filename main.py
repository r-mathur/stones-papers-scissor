from tkinter import *
import random

root = Tk()

root.iconbitmap(r'images/rock.ico')
root.title("Rock | Paper | Scissor")
root.resizable(width=False,height=False)


rock_HandPhoto = PhotoImage(file=r'images/rock_hand.png')
paper_HandPhoto = PhotoImage(file=r'images/paper_hand.png')				#hand photos
scissor_HandPhoto = PhotoImage(file=r'images/scissor_hand.png')

rockPhoto = PhotoImage(file=r'images/rock.png') 
paprtPhoto = PhotoImage(file=r'images/paper.png')		#element photo
scissorPhoto = PhotoImage(file=r'images/scissors.png')



winPhoto = PhotoImage(file=r'images/win.png')
losePhoto = PhotoImage(file=r'images/lose.png')		#result photo
tiePhoto = PhotoImage(file=r'images/tie.png')


rock_HandButton = ''
paper_HandButton = ''
scissor_HandButton = ''

def start():

	global rock_HandButton,paper_HandButton,scissor_HandButton

	rock_HandButton = Button(root,image=rock_HandPhoto,command=lambda:user_pick('rock'))

	paper_HandButton = Button(root,image=paper_HandPhoto,command = lambda:user_pick('paper'))

	scissor_HandButton = Button(root,image=scissor_HandPhoto,command =lambda:user_pick('scissors'))


	rock_HandButton.grid(row = 0, column =0) 
	paper_HandButton.grid(row = 0, column =1)
	scissor_HandButton.grid(row = 0, column =2)


start()
 


def pc_pick():

	choice = random.choice(['rock','paper','scissors'])


#def user_pick(user_choice):















root.mainloop()