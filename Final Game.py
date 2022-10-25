#Semester Project =====> TIC.TAC.TOE GAME

board=["-","-","-","-","-","-","-","-","-"]

def print_board():         #starting with 0-8 because 1-9 giving index error, keep in mind 
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("--","---","---")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("--","---","---")    
    print(board[6]+" | "+board[7]+" | "+board[8])

def player_1_turn():
    position_p1=eval(input("Enter position:1-9:  "))
    if position_p1 not in [1,2,3,4,5,6,7,8,9]:
            while position_p1 not in [1,2,3,4,5,6,7,8,9]:
                print("Such position doesn't exist on the Grid")
                print_board()
                position_p1=(input("RE-enter position:1-9:  "))
                if position_p1 in [1,2,3,4,5,6,7,8,9]:
                    break
    position_p1=int(position_p1)
    position_p1=position_p1-1

    while True:
        if position_p1 in range(0,1):
            while True:
                if 0==position_p1 and board[0]=="-" and board[0]=="-":
                    board[0]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

        if position_p1 in range(1,2):            
            while True:    
                if 1==position_p1 and board[1]=="-" and board[1]=="-":
                    board[1]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

        if position_p1 in range(2,3):   
            while True:
                if 2==position_p1 and board[2]=="-" and board[2]=="-":
                    board[2]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

        if position_p1 in range(3,4):        
            while True:
                if 3==position_p1 and board[3]=="-" and board[3]=="-":
                    board[3]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

        if position_p1 in range(4,5):
            while True:
                if 4==position_p1 and board[4]=="-" and board[4]=="-":
                    board[4]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

        if position_p1 in range(5,6):        
            while True:
                if 5==position_p1 and board[5]=="-" and board[5]=="-":
                    board[5]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

        if position_p1 in range(6,7):
            while True:    
                if 6==position_p1 and board[6]=="-" and board[6]=="-":
                    board[6]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

        if position_p1 in range(7,8):   
            while True:
                if 7==position_p1 and board[7]=="-" and board[7]=="-":
                    board[7]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

        if position_p1 in range(8,9):
            while True:
                if 8==position_p1 and board[8]=="-" and board[8]=="-":
                    board[8]=sign_1
                    return False
                else:
                    print("Position is already occupied")
                    position_p1=(input("Enter position:1-9:  "))
                    if position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p1 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p1=(input("RE-enter position:1-9:  "))
                            if position_p1 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p1=int(position_p1)
                                    position_p1=position_p1-1
                                    break
                    else:
                        position_p1=int(position_p1)
                        position_p1=position_p1-1
                    break

def player_2_turn():
    position_p2=(input("Enter position:1-9:  "))
    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
            while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                print("Such position doesn't exist on the Grid")
                print_board()
                position_p2=(input("RE-enter position:1-9:  "))
                if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                    break
    position_p2=int(position_p2)
    position_p2=position_p2-1

    while True:
        if position_p2 in range(0,1):
            while True:
                if 0==position_p2 and board[0]=="-" and board[0]=="-":
                    board[0]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

        if position_p2 in range(1,2):            
            while True:    
                if 1==position_p2 and board[1]=="-" and board[1]=="-":
                    board[1]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

        if position_p2 in range(2,3):   
            while True:
                if 2==position_p2 and board[2]=="-" and board[2]=="-":
                    board[2]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

        if position_p2 in range(3,4):        
            while True:
                if 3==position_p2 and board[3]=="-" and board[3]=="-":
                    board[3]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

        if position_p2 in range(4,5):
            while True:
                if 4==position_p2 and board[4]=="-" and board[4]=="-":
                    board[4]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

        if position_p2 in range(5,6):        
            while True:
                if 5==position_p2 and board[5]=="-" and board[5]=="-":
                    board[5]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

        if position_p2 in range(6,7):
            while True:    
                if 6==position_p2 and board[6]=="-" and board[6]=="-":
                    board[6]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

        if position_p2 in range(7,8):   
            while True:
                if 7==position_p2 and board[7]=="-" and board[7]=="-":
                    board[7]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

        if position_p2 in range(8,9):
            while True:
                if 8==position_p2 and board[8]=="-" and board[8]=="-":
                    board[8]=sign_2
                    return False
                else:
                    print("Position is already occupied")
                    position_p2=(input("Enter position:1-9:  "))
                    if position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                        while position_p2 not in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                            print("Such position doesn't exist on the Grid")
                            print_board()
                            position_p2=(input("RE-enter position:1-9:  "))
                            if position_p2 in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]:
                                    position_p2=int(position_p2)
                                    position_p2=position_p2-1
                                    break
                    else:
                        position_p2=int(position_p2)
                        position_p2=position_p2-1
                    break

def Comp_Turn():
    while True:
        if board[0]=="-":
            board[0]=sign_2
            break
        if board[1]=="-":
            board[1]=sign_2
            break
        if board[2]=="-":
            board[2]=sign_2
            break
        if board[3]=="-":
            board[3]=sign_2
            break
        if board[4]=="-":
            board[4]=sign_2
            break
        if board[5]=="-":
            board[5]=sign_2
            break
        if board[6]=="-":
            board[6]=sign_2
            break
        if board[7]=="-":
            board[7]=sign_2
            break
        if board[8]=="-":
            board[8]=sign_2
            break

def Comp_Moves_1():
    if board[4]=="-":
        print("Computer's Turn")
        print("")
        board[4]=sign_2
        print_board()
    print(p_name,"'s Turn")
    print("")
    player_1_turn()
    print_board()
    print("")
    print("Comp's Turn")
    #Corners
    if board[0]==sign_1 and board[6]=="-":
        board[6]=sign_2
        print_board()
        print("")
        while True and "-" in board:
            print(p_name,"'s Turn")
            print("")
            player_1_turn()
            print_board()
            print("Comp's Turn")
            print("")
            if board[2]==sign_1 and board[1]=="-":
                board[1]=sign_2
                print_board()
            elif board[1]==sign_1 and board[2]=="-":
                board[2]=sign_2
                print_board()
            elif board[2]==sign_1 and board[5]!="-" and board[8]=="-":
                board[8]=sign_2
                print_board()
            elif board[2]==sign_1 and board[8]!="-" and board[5]=="-":
                board[5]=sign_2
                print_board()
            else:
                Comp_Turn()
                print_board()
            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                print_board()
                print("")
                print("Comp Won")
                return False

    if board[2]==sign_1 and board[0]=="-":
        board[0]=sign_2
        print_board()
        while True and "-" in board:
            print(p_name,"'s Turn")
            print("")
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[8]==sign_1 and board[5]=="-":
                board[5]=sign_2
                print_board()
            elif board[5]==sign_1 and board[8]=="-":
                board[8]=sign_2
                print_board()
            elif board[8]==sign_1 and board[7]!="-" and board[6]=="-":
                board[6]=sign_2
                print_board()
            elif board[8]==sign_1 and board[6]!="-" and board[7]=="-":
                board[7]=sign_2
                print_board()
            else:
                Comp_Turn()
                print_board()
            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                print_board()
                print("")
                print("Comp Won")
                return False

    if board[6]==sign_1 and board[0]=="-":
        board[0]=sign_2
        print_board()
        print("")
        while True and "-" in board:
            print(p_name,"'s Turn")
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[8]==sign_1 and board[7]=="-":
                board[7]=sign_2
                print_board()
            elif board[7]==sign_1 and board[8]=="-":
                board[8]=sign_2
                print_board()
            elif board[8]==sign_1 and board[2]=="-" and board[5]!="-":
                board[2]=sign_2
                print_board()
            elif board[8]==sign_2 and board[2]!="-" and board[5]=="-":
                board[5]=sign_2
                print_board()
            else:
                Comp_Turn()
                print_board()
            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                print_board()
                print("")
                print("Comp Won")
                return False

    if board[8]==sign_1 and board[2]=="-":
        board[2]=sign_2
        print_board()
        print("")
        while True and "-" in board:
            print(p_name,"'s Turn")
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[6]==sign_1 and board[7]=="-":
                board[7]=sign_2
                print_board()
            elif board[7]==sign_1 and board[6]=="-":
                board[6]=sign_2
                print_board()
            elif board[6]==sign_1 and board[0]=="-" and board[1]!="-":
                board[0]=sign_2
                print_board()
            elif board[6]==sign_2 and board[1]=="-" and board[0]!="-":
                board[1]==sign_2
                print_board()
            else:
                Comp_Turn()
                print_board()
            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                print_board()
                print("")
                print("Comp Won")
                return False

    #Rest
    if board[1]==sign_1 and board[0]=="-":
        board[0]=sign_2
        print_board()
        while True and "-" in board:
            print("")
            print(p_name,"'s Turn")
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[8]=="-":
                board[8]=sign_2
                print_board()
            elif board[8]==sign_1 and board[5]=="-":
                board[5]=sign_2
                print_board()
            elif board[3]=="-" and board[4]==board[5]:
                board[3]==sign_2
                print_board()
            elif board[8]==sign_1 and board[6]!="-" and board[7]=="-":
                board[7]=sign_2
                print_board()
            elif board[8]==sign_1 and board[6]=="-" and board[7]!="-":
                board[6]=sign_2
                print_board()
            else:
                Comp_Turn()
                print_board()
            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                print_board()
                print("")
                print("Comp Won")
                return False

    if board[3]==sign_1 and board[0]=="-":
        board[0]=sign_2
        print_board()
        while True and "-" in board:
            print("")
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[8]=="-":
                board[8]=sign_2
                print_board()
            elif board[8]==sign_1 and board[5]=="-":
                board[5]=sign_2
                print_board()
            elif board[6]==sign_1 and board[7]=="-":
                board[7]=sign_2
                print_board()
            elif board[7]==sign_1 and board [6]=="-":
                board[6]==sign_2
                print_board()
            else:
                Comp_Turn()
                print_board()
            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                print_board()
                print("")
                print("Comp Won")
                return False

    if board[5]==sign_1 and board[0]=="-":
        board[0]=sign_2
        print_board()
        while True and "-" in board:
            print("")
            print(p_name,"'s Turn")
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[8]=="-":
                board[8]=sign_2
                print_board()
            elif board[8]==sign_1 and board[2]=="-":
                board[2]=sign_2
                print_board()
            elif board[8]==sign_1 and board[6]=="-":
                board[6]=sign_2
                print_board()
            elif board[8]==sign_1 and board[1]=="-":
                board[1]=sign_2
                print_board()
            else:
                Comp_Turn()
                print_board()
            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                print_board()
                print("")
                print("Comp won")
                return False

    if board[7]==sign_1 and board[8]=="-":
        board[8]=sign_2
        print_board()
        while True and "-" in board:
            print("")
            print(p_name,"'s Turn")
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[0]=="-":
                board[0]=sign_2
                print_board()
            elif board[0]==sign_1 and board[6]=="-":
                board[6]=sign_2
                print_board()
            elif board[1]==sign_1 and board[2]=="-":
                board[2]=sign_2
                print_board()
            elif board[2]==sign_1 and board[1]=="-":
                board[1]=sign_2
                print_board()
            else:
                Comp_Turn()
                print_board()
            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                print_board()
                print("")
                print("Comp Won")
                return False

def Comp_Moves_2():
    y=0
    while y==0:
        print_board()
        print("")
        print(p_name,"'s Turn")
        player_1_turn()
        print_board()
        print('')
        print("Comp's Turn")
        print("")
        if board[1]==sign_1 and "-" in board:
            board[7]=sign_2
            while y==0:
                print(p_name,"'s Turn")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[6]=="-" and board[2]==sign_1:
                    board[6]=sign_2
                    print_board()
                elif board[2]=="-" and board[6]==sign_1:
                    board[2]=sign_2
                    print_board()
                elif board[3]=="-" and board[5]==sign_1:
                    board[3]=sign_2
                    print_board()
                elif board[5]=="-" and board[3]==sign_1:
                    board[5]=sign_2
                    print_board()
                else:
                    board[5]=sign_2
                    print_board()
                if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                    print_board()
                    print("")
                    print("Comp Won")
                    y=1
                    break
                    
                if "-" not in board:
                    print("Tie")
                    y=1
                    break

        if board[2]==sign_1 and "-" in board:
            board[6]=sign_2
            print_board()
            print(p_name,"'s Turn")
            print_board()
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[3]=="-":
                board[3]=sign_2
                print_board()
                print("Comp Wins")
                break
            else:
                board[5]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[1]=="-":
                    board[1]=sign_2
                    print_board()
                    print(p_name,"'s Turn")
                    player_1_turn()
                    print_board()
                    print("Tie")
                    break
                else:
                    board[7]=sign_2
                    print_board()
                    print(p_name,"'s Turn")
                    player_1_turn()
                    print_board()
                    print("Tie")
                    break
           

        if board[3]==sign_1 and "-" in board:
            board[5]=sign_2
            print_board()
            print("")
            print(p_name,"'s Turn")
            print("")
            print_board()
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            if board[1]==sign_1:
                board[7]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print("")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[3]==sign_1:
                    board[6]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    print("")
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break
                else:
                    board[3]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    print("")
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break

            elif board[7]==sign_1:
                board[1]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print("")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[3]==sign_1:
                    board[6]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    print("")
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break
                else:
                    board[3]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break
            
            elif board[2]==sign_1:
                board[6]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print("")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[1]=="-":
                    board[1]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break
                else:
                    board[7]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break
            
            elif board[6]==sign_1:
                board[2]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print("")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[1]=="-":
                    board[1]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    player_1_turn()
                    print("")
                    print("Tie")
                    y=1
                    break
                else:
                    board[7]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    player_1_turn()
                    print("")
                    print("Tie")
                    y=1
                    break

            elif board[8]==sign_1:
                board[1]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print("")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[2]=="-":
                    board[2]=sign_2
                    print_board()
                    print("")
                    print("Comp Won")
                    y=1
                    break
                else:
                    board[6]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break

        if board[5]==sign_1 and "-" in board:
            board[3]=sign_2
            print_board()
            print("")
            print(p_name,"'s Turn")
            print("")
            print_board()
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[6]=="-":
                board[6]=sign_2
                print_board()
                print("")
                print("Comp Won")
                y=1
                break
            else:
                board[2]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print("")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[1]=="-":
                    board[1]=sign_2
                    print_board()
                    print("")
                    print("Comp Won")
                    print('')
                    y=1
                    break
                else:
                    board[7]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break

        if board[6]==sign_1 and "-" in board:
            board[2]=sign_2
            print_board()
            print("")
            print(p_name,"'s Turn")
            print("")
            print_board()
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[1]=="-":
                board[1]=sign_2
                print_board()
                print("Comp Wins")
                y=1
                break
            else:
                board[7]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print("")
                print_board()
                print("")
                player_1_turn()
                print_board()
                print("")
                print("Comp'd Turn")
                print("")
                if board[3]=="-":
                    board[3]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print("")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break
                else:
                    board[5]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break

        if board[7]==sign_1 and "-" in board:
            board[1]=sign_2
            print_board()
            print("")
            print(p_name,"'s Turn")
            print("")
            print_board()
            player_1_turn()
            print_board()
            print("")
            print("Comp's Turn")
            print("")
            if board[2]=="-":
                board[2]=sign_2
                print_board()
                print("")
                print("Comp Wins")
                y=1
                break
            else:
                board[6]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[3]=="-":
                    board[3]=sign_2
                    print_board()
                    print("")
                    print("Comp Wins")
                    y=1
                    break
                else:
                    board[5]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Tie")
                    y=1
                    break

        if board[8]==sign_1 and "-" in board:
            board[6]=sign_2
            print_board()
            print("")
            print(p_name,"'s Turn")
            print_board()
            player_1_turn()
            print_board
            print("")
            print("Comp's Turn")
            print("")
            if  board[3]=="-":
                board[3]=sign_2
                print_board()
                print("")
                print("Comp Wins")
                y=1
                break
            else:
                board[5]=sign_2
                print_board()
                print("")
                print(p_name,"'s Turn")
                print_board()
                player_1_turn()
                print_board()
                print("")
                print("Comp's Turn")
                print("")
                if board[1]=="-":
                    board[1]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Comp's Turn")
                    print("")
                    if board[2]=="-":
                        board[2]=sign_2
                        print_board()
                        print("")
                        print("Comp Wins")
                        y=1
                        break
                    else:
                        board[7]=sign_2
                        print_board()
                        print("")
                        print("Tie")
                        y=1
                        break
                else:
                    board[7]=sign_2
                    print_board()
                    print("")
                    print(p_name,"'s Turn")
                    print_board()
                    player_1_turn()
                    print_board()
                    print("")
                    print("Comp's Turn")
                    print("")
                    if board[1]=="-":
                        board[1]=sign_2
                        print_board()
                        print("")
                        print("Tie")
                        y=1
                        break
                    else:
                        board[2]=sign_2
                        print_board()
                        print("")
                        print("Tie")
                        y=1
                        break

def Comp_Moves_3():
    while True:
        if board[7]==sign_1:
            Comp_Turn()
            break
        if board[1]==sign_1:
            Comp_Turn()
            break
        if "-" not in board:
            break
        #Rows:
        if board[0]==board[1]==sign_1 and board[2]=="-":
            board[2]=sign_2
            break
        elif board[1]==board[2]==sign_1 and board[0]=="-":
            board[0]=sign_2
            break
        elif board[2]==board[0]==sign_1 and board[1]=="-":
            board[1]=sign_2
            break

        elif board[3]==board[4]==sign_1 and board[5]=="-":
            board[5]=sign_2
            break
        elif board[4]==board[5]==sign_1 and board[3]=="-":
            board[3]=sign_2
            break
        elif board[5]==board[3]==sign_1 and board[4]=="-":
            board[4]=sign_2
            break

        elif board[6]==board[7]==sign_1 and board[8]=="-":
            board[8]=sign_2
            break
        elif board[7]==board[8]==sign_1 and board[6]=="-":
            board[6]=sign_2
            break
        elif board[8]==board[6]==sign_1 and board[7]=="-":
            board[7]=sign_2
            break

        #Columns
        elif board[0]==board[3]==sign_1 and board[6]=="-":
            board[6]=sign_2
            break
        elif board[3]==board[6]==sign_1 and board[0]=="-":
            board[0]=sign_2
            break
        elif board[6]==board[0]==sign_1 and board[3]=="-":
            board[3]=sign_2
            break

        elif board[1]==board[4]==sign_1 and board[7]=="-":
            board[7]=sign_2
            break
        elif board[4]==board[7]==sign_1 and board[1]=="-":
            board[1]=sign_2
            break
        elif board[7]==board[1]==sign_1 and board[4]=="-":
            board[4]=sign_2
            break

        elif board[2]==board[5]==sign_1 and board[8]=="-":
            board[8]=sign_2
            break
        elif board[5]==board[8]==sign_1 and board[2]=="-":
            board[2]=sign_2
            break
        elif board[8]==board[2]==sign_1 and board[5]=="-":
            board[5]=sign_2
            break

        #Diagonals:
        elif board[0]==board[4]==sign_1 and board[8]=="-":
            board[8]=sign_2
            break
        elif board[4]==board[8]==sign_1 and board[0]=="-":
            board[0]=sign_2
            break
        elif board[8]==board[0]==sign_1 and board[4]=="-":
            board[4]=sign_2
            break

        elif board[2]==board[4]==sign_1 and board[6]=="-":
            board[6]=sign_2
        elif board[4]==board[6]==sign_1 and board[2]=="-":
            board[2]=sign_2
        elif board[6]==board[2]==sign_1 and board[4]=="-":
            board[4]=sign_2
        else:
            Comp_Turn()

while True:
    print("Welcome to Tic Tac Toe Game")
    print("")
    print("------------------")
    print("      Menu")
    print("------------------")
    print("")
    print("1)Select Game Mode\n2)Exit")
    print("")
    menu_select=eval(input("Select 1 or 2: "))
    print("")
    if menu_select==2:
        print("")
        print("GoodBye")
        break
    elif menu_select==1:
        while True:
            print("1)Single Player\n2)Multiplayer\n3)Exit Game")
            print("")
            mode_select=eval(input("Select 1,2, or 3: "))
            print("")
            if mode_select==3:
                print("Exiting Game\nGoodbye")
                play_again="n"
                break
            elif mode_select==1:
                print("Welcome to Single Player Mode")
                print("Enter Players's Name")
                p_name=input("Enter Player's Name: ")
                p_name=p_name.capitalize()
                print("")
                
                while True:
                    print("Hello ",p_name,"\nChoose Your Sign")
                    sign=input("'X' or 'O':  ")
                    if sign=="x" or sign=="X":
                        sign_1="X"
                        sign_2="O"
                        print(p_name,"'s Sign is ",sign_1,"\nComputer's sign is ",sign_2)
                        break
                    elif sign=="O" or sign=="o":
                        sign_1="O"
                        sign_2="X"
                        print(p_name,"'s Sign is ",sign_1,"\nComputer's sign is ",sign_2)
                        break
                    else:
                        print("Invalid Input")
                while True:        
                    print("Now we'll toss to see who's turn is first !!!")
                    import random
                    toss=input(f"{p_name}, Please choose heads or tails:  ")
                    if toss=="heads" or toss=="Heads" or toss=="HEADS":
                        toss_2=random.randint(0,1)
                        if toss_2==0:
                            print("It's heads !!\n",p_name," won the toss !!!")
                            play=1
                            break
                        else:
                            print("It's tails !!\nComp won the toss !!!")
                            play=2
                            break
                    elif toss=="tails" or toss=="Tails" or toss=="TAILS":        
                        toss_2=random.randint(0,1)
                        if toss_2==0:
                            print("It's tails !!.\n",p_name," won the toss !!!")
                            play=1
                            break
                        else:
                            print("It's heads !!.\nComp won the toss !!!") 
                            play=2
                            break
                    else:
                        print("Invalid Input")
                    
                if play==1:
                    #Main Game 2
                    print("Notice: Positions are as:\n1  2  3\n4  5  6\n7  8  9")
                    print("")
                    print_board()
                    print(p_name,"'s Turn")
                    player_1_turn()
                    print_board()
                    print("")
                    print("Comp's Turn")
                    print("")
                    if board[4]==sign_1:
                        board[0]=sign_2
                        print_board()
                        print("")
                        Comp_Moves_2()
                    else:
                        board[4]=sign_2
                        print_board()
                        while True:
                            print(p_name,"'s Turn")
                            player_1_turn()
                            print_board()
                            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                                        print_board()
                                        print("")
                                        print("Comp Won")
                                        break
                            if "-" not in board:
                                print("Tie")
                                break
                            print("")
                            print("Comp's Turn")
                            Comp_Moves_3()
                            print_board()
                            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                                        print_board()
                                        print("")
                                        print("Comp Won")
                                        break
                            if "-" not in board:
                                print("Tie")
                                break

                elif play==2:
                    #Main Game
                    Comp_Moves_1()
                    if "-" not in board and True:
                        print("Tie")

                play_again=input("Do you want to play again?\nSelect y or n: ") 
                if play_again=="y" or play_again=="Y" or play_again=="yes" or play_again=="Yes" or play_again=="YES":
                    board=["-","-","-","-","-","-","-","-","-"]
                    print("Starting Again")
                elif play_again=="n" or play_again=="N" or play_again=="no" or play_again=="No" or play_again=="NO":
                    print("GoodBye")
                    break
                else:
                    print("Invalid Input")
                    print("")
                    play_again="n"

            elif mode_select==2:
                print("")
                print("Welcome to Multiplayer Mode")
                print("Enter Players's Name")
                p1_name=input("Enter Player 1 Name: ")
                p1_name=p1_name.capitalize()
                p2_name=input("Enter Player 2 Name: ")
                p2_name=p2_name.capitalize()
                print("Hello ",p1_name," and ",p2_name)
                while True:
                    print("Player 1\nSelect Your Sign:")
                    sign=input("X or O: ")
                    if sign=="x" or sign=="X":
                        sign_1="X"
                        print(p1_name,"'s sign is 'X' ")
                        print(p2_name,"'s sign is 'O' ")
                        sign_2="O"
                        break
                    elif sign=="O" or sign=="o":
                         sign_1="O"
                         print(p1_name,"'s sign is 'O' ") 
                         print(p2_name,"'s sign is 'X' ")
                         sign_2="X"
                         break
                    else:
                        print("Invalid Input")
                    print("")
                while True:        
                    print("Now we'll toss to see who's turn is first !!!")
                    import random
                    toss=input(f"{p1_name}, Please choose heads or tails:  ")
                    if toss=="heads" or toss=="Heads" or toss=="HEADS":
                        toss_2=random.randint(0,1)
                        if toss_2==0:
                            print("It's heads !!\n",p1_name," won the toss !!!")
                            play=1
                            break
                        else:
                            print("It's tails !!\n",p2_name," won the toss !!!")
                            play=2
                            break
                    elif toss=="tails" or toss=="Tails" or toss=="TAILS":        
                        toss_2=random.randint(0,1)
                        if toss_2==0:
                            print("It's tails !!.\n",p1_name," won the toss !!!")
                            play=1
                            break
                        else:
                            print("It's heads !!.\n",p2_name," won the toss !!!") 
                            play=2
                            break
                    else:
                        print("Invalid Input")

                if play==1:
                        print(p1_name,"'s turn is first")
                        #Main Game
                        while True:
                            print("")
                            print("Positions are as follows: \n 1  2  3\n 4  5  6\n 7  8  9")
                            print("")
                            print_board()
                            print("")
                            print(p1_name,"'s turn")
                            print("")
                            player_1_turn()
                            print("")
                            if (board[0]==board[1]==board[2]==sign_1) or (board[3]==board[4]==board[5]==sign_1) or (board[6]==board[7]==board[8]==sign_1) or (board[0]==board[3]==board[6]==sign_1) or (board[1]==board[4]==board[7]==sign_1) or (board[2]==board[5]==board[8]==sign_1) or (board[0]==board[4]==board[8]==sign_1) or (board[2]==board[4]==board[6]==sign_1):
                                print_board()
                                print("")
                                print(p1_name," won")
                                break
                            if "-" not in board:
                                print("It's a Tie")
                                print("")
                                break
                            print("")
                            print_board()
                            print("")
                            print(p2_name,"'s turn")
                            player_2_turn()
                            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                                print_board()
                                print(p2_name," won")
                                break
                            if "-" not in board:
                                print("It's a Tie")
                                print("")
                                break
                        
                elif play==2:
                        print("")
                        print("Positions are as follows: \n 1  2  3\n 4  5  6\n 7  8  9")
                        print("")
                        print(p2_name,"'s turn is first! ")
                        #Main Game
                        #Main Game
                        while True:
                            print_board()
                            print("")
                            print(p2_name,"'s turn")
                            print("")
                            player_2_turn()
                            if (board[0]==board[1]==board[2]==sign_2) or (board[3]==board[4]==board[5]==sign_2) or (board[6]==board[7]==board[8]==sign_2) or (board[0]==board[3]==board[6]==sign_2) or (board[1]==board[4]==board[7]==sign_2) or (board[2]==board[5]==board[8]==sign_2) or (board[0]==board[4]==board[8]==sign_2) or (board[2]==board[4]==board[6]==sign_2):
                                print_board()
                                print("")
                                print(p2_name," won")
                                break
                            if "-" not in board:
                                print("It's a Tie")
                                print("")
                                break
                            print("")
                            print_board()
                            print("")
                            print(p1_name,"'s turn")
                            print("")
                            player_1_turn()
                            print("")
                            if (board[0]==board[1]==board[2]==sign_1) or (board[3]==board[4]==board[5]==sign_1) or (board[6]==board[7]==board[8]==sign_1) or (board[0]==board[3]==board[6]==sign_1) or (board[1]==board[4]==board[7]==sign_1) or (board[2]==board[5]==board[8]==sign_1) or (board[0]==board[4]==board[8]==sign_1) or (board[2]==board[4]==board[6]==sign_1):                                
                                print("")
                                print_board()
                                print(p1_name," won")
                                break
                            if "-" not in board:
                                print("It's a Tie")
                                print("")
                                break
                         
                play_again=input("Do you want to play again?\nSelect y or n: ") 
                if play_again=="y" or play_again=="Y" or play_again=="yes" or play_again=="Yes" or play_again=="YES":
                    board=["-","-","-","-","-","-","-","-","-"]
                    print("Starting Again")
                elif play_again=="n" or play_again=="N" or play_again=="no" or play_again=="No" or play_again=="NO":
                    print("GoodBye")
                    break
                else:
                    print("Invalid Input")
                    print("")
                    play_again="n"
            if play_again=="n" or play_again=="N" or play_again=="no" or play_again=="No" or play_again=="NO":
                break
        if play_again=="n" or play_again=="N" or play_again=="no" or play_again=="No" or play_again=="NO":
                break
                  
    else:
        print("Invalid Input")
        
    