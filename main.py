from tkinter import * 
from tkinter import simpledialog
from tkinter import messagebox
from decimal import Decimal
from functions import ajustar_precios, ajustar_precios_con_IVA


# Config of the Window
window = Tk()

window.title('Item Price Calculator')
window.geometry('200x110') # Default size of the window

initial_width = 200
initial_height = 110

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - initial_width) // 2
y = (screen_height - initial_height) // 2

window.geometry(f'{initial_width}x{initial_height}+{x}+{y}')
# window.iconbitmap('src\\icon.ico')
# window.attributes('-topmost',True)
# window.minsize(800, 370) # Minimun size of the window
# window.maxsize(800, 370) # Maximun size of the window



row_quantity_title_label = Label(window, text='Row Quantity', font=('Arial', 12 ), width=12, borderwidth=1, relief='ridge')
row_quantity_entry = Entry(window, bg='white', width=10, font=('Arial', 12),justify='right')
calculate_btn = Button(window, text='Calculate', font=('Arial', 8), width=7, command= lambda: creation_of_Rows(int(row_quantity_entry.get())))
row_quantity_entry.focus_force()

# TODO Make the version a button to open a About me info.
version_label = Label(window, text='Version 0.4', font=('Arial', 7))
# // TODO Display valor neto
# // TODO Make smaller the Labels of the program.


def creation_of_Rows(event):


    ## Function to display a little window where a prompt is going to be displayed asking for quantities or values to be used as prices.
    def custom_dialog_question(prompt, parent):
        # Created a custom window for the questions.

        dialog = Toplevel(parent)
        question_window_width = 200
        question_window_height = 120

        # Values to display the window on the center of the screen.
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()


        x = round((screen_width - question_window_width) / 2)
        y = round((screen_height - question_window_height) / 2)

        #// TODO Make the question window centered no matter what res. WIP
        #// TODO Make Calculate New Price button, actually place the new
        #// TODO prices in the the Entries and Labels.

        dialog.geometry(f'{question_window_width}x{question_window_height}+{x}+{y}')
        
        # dialog.geometry('200x120+500+150')
        dialog.transient(parent)  # Hacer que el diálogo dependa de la ventana principal
        dialog.grab_set()  # Bloquear la interacción con la ventana principal
        dialog.focus_force()  # Forzar el foco en el diálogo

        # Configurar el diálogo
        Label(dialog, text=prompt).pack(padx=10, pady=10)
        entry = Entry(dialog)
        entry.pack(padx=10, pady=10)
        entry.focus_force()  # Foco en el campo de entrada

        # Variable para almacenar el valor ingresado
        result = []

        # Función para capturar el valor y cerrar el diálogo
        def on_ok(event):
            try:
                result.append(entry.get())
            except ValueError:
                result.append(None)
            dialog.destroy()

        # Botón OK
        Button(dialog, text="OK", command=on_ok).pack(pady=10)
        entry.bind("<Return>", on_ok)
        # Espera hasta que el usuario cierre el diálogo
        parent.wait_window(dialog)

        # Retorna el resultado
        return result[0] if result else None

    def calculate(total_price, desired_total, values, quantity, row_question):
        
            # TODO Make a condition when the price desired and the total are the same
            # TODO Make the calculations when the order has IVA
 
            if total_price != desired_total:
                if IVA_question == 'no':
                    # Calculation of the new prices.
                    ajusted_values = ajustar_precios(desired_total, values)
                    
                    # Addition of all values into one. 
                    total_price = sum(Decimal(valor) for valor in ajusted_values)
                    
                    new_sub_total_label.config(text=f'{round(total_price,2)}')  
                    new_total_label.config(text=f'{round(total_price,2)}')  
                    new_iva_label.config(text=f'{0.00}')  
                    
                
                    for x in range(row_question):
                        
                        result = ajusted_values[x] / quantity[x]

                        new_quantity_entries[x].insert(0, quantity[x])
                        new_cost_entries[x].insert(0, round(result,2))
                        new_net_worth_labels[x].config(text=f'{round(ajusted_values[x],2)}')
                    
                if IVA_question == 'yes':
                    # Calculation of the new prices.
                    ajusted_values = ajustar_precios_con_IVA(desired_total, values)
                    
                    # Addition of all values into one. 
                    sub_total_price = sum(Decimal(valor) for valor in ajusted_values)
                    iva = sub_total_price * Decimal(0.16)
                    total = sub_total_price + iva

                    new_sub_total_label.config(text=f'{round(sub_total_price,2)}')  
                    new_iva_label.config(text=f'{round(iva ,2)}')
                    new_total_label.config(text=f'{round(total,2)}')

                    
                    for x in range(row_question):
                        new_quantity_entries[x].delete(0, END)
                        new_cost_entries[x].delete(0, END)
                        new_net_worth_labels[x].config(text=f'')
                    
                    for x in range(row_question):
                        
                        result = ajusted_values[x] / quantity[x]


                        new_quantity_entries[x].insert(0, quantity[x])
                        new_cost_entries[x].insert(0, round(result,2))
                        new_net_worth_labels[x].config(text=f'{round(ajusted_values[x],2)}')


            else: 
                
                messagebox.showinfo('', 'The price desire is the same as the initial price.')
            
            return total_price, desired_price, cost_entries_Decimals, quantity_entries_Decimals
        


            # for item in enumerate(new_cost_entries):
                # if cost_question is not None:
                    # new_cost_entries[item].insert(0, cost_question)
        
    def reset():

        for x in range(row_quantity):

            row_tittle_label.grid_forget()
            quantity_tittle_label.grid_forget()
            cost_title_label.grid_forget()
            net_worth_title_label.grid_forget()

            row_labels[x].grid_forget()
            quantity_entries[x].grid_forget()
            cost_entries[x].grid_forget()
            net_worth_entries[x].grid_forget()
            
            sub_total_title_label.grid_forget()
            sub_total_label.grid_forget()

            iva_title_label.grid_forget()
            iva_label.grid_forget()

            total_title_label.grid_forget()
            total_label.grid_forget()

            desired_total_label.grid_forget()
            desired_total_entry.grid_forget()

            new_price_calculate_btn.grid_forget()
            reset_btn.grid_forget()

            version_label.grid_forget()

            ##################################

            new_row_labels[x].grid_forget() 
            new_quantity_entries[x].grid_forget()
            new_cost_entries[x].grid_forget()
            new_net_worth_labels[x].grid_forget()
            
            new_row_tittle_label.grid_forget()
            new_quantity_tittle_label.grid_forget()
            new_cost_title_label.grid_forget()
            new_net_worth_title_label.grid_forget()

            new_sub_total_title_label.grid_forget()
            new_sub_total_label.grid_forget()

            new_iva_title_label.grid_forget()
            new_iva_label.grid_forget()

            new_total_title_label.grid_forget()
            new_total_label.grid_forget()

            ###################################
            window.geometry('200x110')
            x = (screen_width - initial_width) // 2
            y = (screen_height - initial_height) // 2

            window.geometry(f'{initial_width}x{initial_height}+{x}+{y}')

            window.grid_columnconfigure(0, minsize=200)
            row_quantity_entry.delete(0, END)
            row_quantity_entry.focus_force()

            row_quantity_title_label.grid(row=0 ,column=0, pady=2)
            row_quantity_entry.grid(row=1, column=0, pady=2)
            calculate_btn.grid(row=2, column=0, pady=2)

            version_label.grid(row=8, column=0)

        
    row_quantity = int(row_quantity_entry.get())
    
    # Code to center the window on the middle of the screen
    # No matter what resolution the window is displaying.
    width = 940
    height = 330

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}') # Default size of the window
    

    # Main Variables.
    global new_cost_entries, new_quantity_entries
    row_labels = []
    quantity_entries = []
    quantity_entries_Decimals = []
    cost_entries = []
    net_worth_entries = []
    cost_entries_Decimals = []
    # new_net_worth_Decimals = []
    
    new_row_labels = []
    new_quantity_entries = []
    new_cost_entries = []
    new_net_worth_labels = []

    net_worth_result = []

    # Widgets
    # Labels
    
    # Creation of the initial labels to be displayed on the GUI.

    # # Old
    row_tittle_label = Label(window, text='Row', font=('Arial', 12 ), width=6, borderwidth=1, relief='ridge')
    quantity_tittle_label = Label(window, text='Quantity', font=('Arial', 12 ), width=10, borderwidth=1, relief='ridge')
    cost_title_label = Label(window, text='Cost', font=('Arial', 12 ), width=10, borderwidth=1, relief='ridge')
    net_worth_title_label = Label(window, text='Net Cost', font=('Arial', 12 ), width=10, borderwidth=1, relief='ridge')

    sub_total_title_label = Label(window, text='Sub Total', font=('Arial', 12 ), width=8, borderwidth=1, relief='ridge')
    iva_title_label = Label(window, text='IVA', font=('Arial', 12 ), width=8, borderwidth=1, relief='ridge')
    total_title_label = Label(window, text='Total', font=('Arial', 12 ), width=8, borderwidth=1, relief='ridge')

    sub_total_label = Label(window, bg='white', width=10, anchor=E)
    iva_label = Label(window, bg='white', width=10, anchor=E)
    total_label = Label(window, bg='white', width=10, anchor=E)


    # # Positions
    row_tittle_label.grid(row=1, column=0)
    quantity_tittle_label.grid(row=1, column=1)
    cost_title_label.grid(row=1, column=2)
    net_worth_title_label.grid(row=1, column=3)

    sub_total_title_label.grid(row=3, column=4)
    sub_total_label.grid(row=4, column=4)

    iva_title_label.grid(row=5, column=4)
    iva_label.grid(row=6, column=4)

    total_title_label.grid(row=7, column=4)
    total_label.grid(row=8, column=4)


    # # New
    new_row_tittle_label = Label(window, text='Row', font=('Arial', 12 ), width=6, borderwidth=1, relief='ridge')
    new_quantity_tittle_label = Label(window, text='Quantity', font=('Arial', 12 ), width=8, borderwidth=1, relief='ridge')
    new_cost_title_label = Label(window, text='Cost', font=('Arial', 12 ), width=10, borderwidth=1, relief='ridge')
    new_net_worth_title_label = Label(window, text='Net Cost', font=('Arial', 12 ), width=10, borderwidth=1, relief='ridge')
    
    new_sub_total_title_label = Label(window, text='Sub Total', font=('Arial', 12 ), width=8, borderwidth=1, relief='ridge')
    new_iva_title_label = Label(window, text='IVA', font=('Arial', 12 ), width=8, borderwidth=1, relief='ridge')
    new_total_title_label = Label(window, text='Total', font=('Arial', 12 ), width=8, borderwidth=1, relief='ridge')

    new_sub_total_label = Label(window, bg='white', width=10, anchor=E)
    new_iva_label = Label(window, bg='white', width=10, anchor=E)
    new_total_label = Label(window, bg='white', width=10, anchor=E)

    
    desired_total_label = Label(window, width=10, text='Desired Total: ')
    desired_total_entry = Entry(window, width=10, bg='white', justify='right')
    
    new_price_calculate_btn = Button(window, text='Calculate\nNew Price', font=('Arial', 8), width=12, command= NONE)
    reset_btn = Button(window, text='Reset', font=('Arial', 8), width=8, command= NONE)

    # # Positions
    new_row_tittle_label.grid(row=1, column=6)
    new_quantity_tittle_label.grid(row=1, column=7)
    new_cost_title_label.grid(row=1, column=8)
    new_net_worth_title_label.grid(row=1, column=9)

    new_sub_total_title_label.grid(row=3, column=10)
    new_sub_total_label.grid(row=4, column=10)

    new_iva_title_label.grid(row=5, column=10)
    new_iva_label.grid(row=6, column=10)

    new_total_title_label.grid(row=7, column=10)
    new_total_label.grid(row=8, column=10)


    window.grid_columnconfigure(0, minsize=0)
    window.grid_columnconfigure(5, minsize=100)
    window.grid_columnconfigure(10, minsize=15)

    row_quantity_title_label.grid_forget()
    row_quantity_entry.grid_forget()
    calculate_btn.grid_forget()
    
    ## For loop to configurate the position of the labels and entries where the quantities, prices and net worth are going
    # to be displayed. Depending on the number of rows the order has.
    for rows in range(row_quantity): 
        # Old
        row_label = Label(window, text= rows+1, width=5)
        row_label.grid(row=rows+2, column=0)
        row_labels.append(row_label)
         
        
        quantity_entry2 = Entry(window, width=10, bg='white', justify='right')
        quantity_entry2.grid(row=rows+2, column=1)
        quantity_entries.append(quantity_entry2)

        cost_entry2 = Entry(window, width=10, bg='white', justify='right' )
        cost_entry2.grid(row=rows+2, column=2)
        cost_entries.append(cost_entry2)

        net_worth_label = Label(window, width=10, bg='white', anchor=E, borderwidth=1, relief='ridge' )
        net_worth_label.grid(row=rows+2, column=3)
        net_worth_entries.append(net_worth_label)

        # New

        new_row_label = Label(window, text= rows+1, width=5)
        new_row_label.grid(row=rows+2, column=6)
        new_row_labels.append(new_row_label)

        new_quantity_entry = Entry(window, width=10, bg='white', justify='right' )
        new_quantity_entry.grid(row=rows+2, column=7)
        new_quantity_entries.append(new_quantity_entry)

        new_cost_entry = Entry(window, width=10, bg='white', justify='right')
        new_cost_entry.grid(row=rows+2, column=8)
        new_cost_entries.append(new_cost_entry)

        new_net_worth_label = Label(window, width=10, bg='white', anchor=E, borderwidth=1, relief='ridge' )
        new_net_worth_label.grid(row=rows+2, column=9)
        new_net_worth_labels.append(new_net_worth_label)

    # For loop to open the custom window to display the prompt.
    for item in range(row_quantity):
        items_question = custom_dialog_question(f'How many items has the row {item+1}: ', window)
        if items_question is not None:  # Verificar si se ingresó un valor
            quantity_entries[item].insert(0, int(items_question))  # Insertar el valor en el Entry correspondiente
            
    # For loop to open the custom window to display the prompt.
    for item in range(row_quantity):
        cost_question = custom_dialog_question(f'What is the cost of the item {item+1}: ', window)
        if cost_question is not None:
            cost_entries[item].insert(0, float(cost_question))
            
    
    # TODO Find a way to do this convertion in just one loop.
    # For loop to convert every value inside of the entry into a Decimal value. 
    for y in quantity_entries: 
        new_value = Decimal(y.get())

        quantity_entries_Decimals.append(new_value)

    # For loop to convert every value inside of the entry into a Decimal value. 
    for x in cost_entries:
        new_value = Decimal(x.get())

        cost_entries_Decimals.append(new_value)

    # For loop to multiply values from 2 list.
    for i in range(0, len(cost_entries_Decimals)):

        result = cost_entries_Decimals[i] * quantity_entries_Decimals[i]
        
        if net_worth_entries is not None:
            net_worth_entries[i].config(text=f'{result}')

        net_worth_result.append(result) 

    
    total_price = sum(Decimal(valor) for valor in net_worth_result) # Comprenhension list to sum all the values of the list.
    
    IVA_question = messagebox.askquestion('','The order has IVA?')

    if IVA_question == 'yes' or IVA_question == 'YES':

        sub_total_label.config(text=f'{total_price}')
        iva_label.config(text=f'{round(total_price*Decimal(0.16),2)}')
        total_label.config(text=f'{total_price + round(total_price*Decimal(0.16),2)}')

        desired_price = simpledialog.askfloat('Input', f'Introduce the desired price: ', parent=window)
        
        desired_total_entry.insert(0, desired_price)
        desired_total_label.grid(row=row_quantity+8, column=5) 
        desired_total_entry.grid(row=row_quantity+9, column=5) 

        new_price_calculate_btn.config(command=lambda: calculate(total_price, float(desired_total_entry.get()), cost_entries_Decimals, quantity_entries_Decimals, row_quantity))
        new_price_calculate_btn.grid(row=row_quantity+10, column=5, pady=5)
        
        reset_btn.config(command=reset)
        reset_btn.grid(row=row_quantity+11, column=5)

    else:
        sub_total_label.config(text=f'{total_price}')
        iva_label.config(text=f'{0.00}')
        total_label.config(text=f'{total_price}')
        
        desired_price = simpledialog.askfloat('Input', f'Introduce the desired price: ', parent=window)
        
        desired_total_entry.insert(0, desired_price)
        desired_total_label.grid(row=row_quantity+8, column=5) 
        desired_total_entry.grid(row=row_quantity+9, column=5) 

        new_price_calculate_btn.config(command=lambda: calculate(total_price, desired_price, cost_entries_Decimals, quantity_entries_Decimals, row_quantity))
        new_price_calculate_btn.grid(row=row_quantity+10, column=5, pady=5)
        
        reset_btn.config(command=reset)
        reset_btn.grid(row=row_quantity+11, column=5)

# Bind of Enter to simply put the value and hit enter to start the function.
row_quantity_entry.bind('<Return>', creation_of_Rows)
    

window.grid_columnconfigure(0, minsize=200)
row_quantity_title_label.grid(row=0 ,column=0, pady=2)
row_quantity_entry.grid(row=1, column=0, pady=2)
calculate_btn.grid(row=2, column=0, pady=2)

version_label.grid(row=8, column=0)


if __name__ == '__main__':
    window.mainloop()