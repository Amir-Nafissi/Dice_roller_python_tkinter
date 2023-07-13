import random
from tkinter import *
window = Tk()
window.title("Dice Roller - Amir Nafissi")

#-----------------function:-----------------

def print_rolls():
  """rolls dice according to the number of sides and number of dice, then places a lable listing the dice rolled with commas in between. If 'show sum' is active, it will turn the list of dice rolled into an equation and will also display the sum.
  """
  
  #getting the rolls:
  final_rolls_list = []
  for i in range (int(entry_number_of_dice.get())):
    roll = random.randint(1, radio_button_status.get() + 1)
    final_rolls_list.append(roll)

  #printing final result:
  final_rolls_string = ""
  if checkbox_status.get() == False:
    for i in range (len(final_rolls_list)):
      final_rolls_string += f"{final_rolls_list[i]},"
    final_rolls_string = final_rolls_string[0:-1]
  elif checkbox_status.get() == True:
    for i in range(len(final_rolls_list)):
      final_rolls_string += f"{final_rolls_list[i]} + " 
    final_rolls_string = final_rolls_string[0:-3]
    x = sum(final_rolls_list)
    final_rolls_string = f"{final_rolls_string} = {x}"

  lable_final["text"] =  f"You rolled {final_rolls_string}"


#-----------------the radio buttons:-----------------
#lable for radio buttons
lable_number_of_sides = Label(window, text = "Number of sides:")
lable_number_of_sides.grid(row = 0, column = 0)

# Creates a variable to keep track of which radio button is selected
radio_button_status = IntVar(value = int(6)) #sets default value to 6

radio_button_for_4 = Radiobutton(window, text = "4", variable = radio_button_status, value = 4)
radio_button_for_4.grid(row = 0, column = 1)

radio_button_for_6 = Radiobutton(window, text = "6", variable = radio_button_status, value = 6)
radio_button_for_6.grid(row = 0, column = 2)

radio_button_for_8 = Radiobutton(window, text = "8", variable = radio_button_status, value = 8)
radio_button_for_8.grid(row = 0, column = 3)

radio_button_for_12 = Radiobutton(window, text = "12", variable = radio_button_status, value = 12)
radio_button_for_12.grid(row = 0, column = 4)

radio_button_for_20 = Radiobutton(window, text = "20", variable = radio_button_status, value = 20)
radio_button_for_20.grid(row = 0, column = 5)

#-----------------the textbox:-----------------
default_num_dice = IntVar(value = int(2))

lable_number_of_dice = Label(window, text = "Number of dice:")
lable_number_of_dice.grid(row = 1, column = 0)

entry_number_of_dice = Entry(window, width = 6, textvariable = default_num_dice)
entry_number_of_dice.grid(row = 1, column = 1)

#-----------------the checkbox:-----------------
checkbox_status = BooleanVar(value = False) #sets default value to False

lable_show_sum = Label(window, text = "Show sum")
lable_show_sum.grid(row = 1, column = 3)

checkbox = Checkbutton(window, variable = checkbox_status)
checkbox.grid(row = 1, column = 4)

#-----------------the button:-----------------
button = Button(window, text = "Roll Dice", command=print_rolls)
button.grid(row = 2, column = 0)

#-----------------the final lable:-----------------
lable_final = Label(window, text = "")
lable_final.grid(row = 2, column = 3)

mainloop()