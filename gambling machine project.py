import random
MAXLINES = 3
MAX_BET = 200
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}
def check_winnings(columns,lines,bet,values):
    winnnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnnings,winning_lines
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for col in range (COLS):
        column = []
    current_symbols = all_symbols[:]
    for row in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
    columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end= "|")
            else:
                print(column[row], end="")
        
        print()
    
        


def deposit():
    while True:
      amount = input("enter your amount $ :" )
      if amount.isdigit():
        amount = int(amount)
        
    
        if amount > 0:
            return amount
        
        else:
            print(" amount  must be greater than 0 please")
      else:
        print("Amount must be greater than 0. Try Again !!.")
    

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAXLINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if  1  <= lines <= MAXLINES :
                return lines
    
        
            else:
                print("Enter a valid number of line")
        else:
            print("Please enter the number")
    return lines
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            
            
           
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    
            
     
def main():       
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        
        if  total_bet > balance:
            print(
                f"You do not have enough to bet that amount,your current balance  is ${balance}")
        else:
            
            break
            
    
   
    print(f"You are betting ${bet} on {lines}.Total bet is equal to ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_values)
    print(f"{winnings}.")
    print(f"You won on lines:",  winning_lines)
    
def games(balance):
    
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        
        if  total_bet > balance:
            print(
                f"You do not have enough to bet that amount,your current balance  is ${balance}")
        else:
            
            break
            
    
   
    print(f"You are betting ${bet} on {lines}.Total bet is equal to ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines:",  winning_lines)
    return winnings - total_bet

def final():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to play( q to quit):")
        if answer == "q":
            break
        balance += games(balance)
    print(f"Youa are left with ${balance}")
         

   
main()
    
        
  
