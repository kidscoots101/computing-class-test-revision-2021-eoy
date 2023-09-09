COMBO_A_COST = [7.90, 11.10, 10.50, 13.80, 28.30, 16.25, 24.90, 31.20, 9.90, 19.80]
COMBO_B_COST = [5.00, 4.75, 4.60, 3.80, 2.50]

total_cost = 0

while True:
    setdone = False 
    
    while not setdone:
        meal_id = input("Enter Meal ID: ")
        meal_group = meal_id[0]
        meal_num = meal_id[1:3]

        if meal_group == "A":
            if 0 < int(meal_num) and int(meal_num) <= len(COMBO_A_COST):
                cost = COMBO_A_COST[int(meal_num) - 1]
                costed = round(cost, 2)
                print("$ {:.2f}".format(costed))
                print(meal_id)
                total_cost += costed
                setdone = True
            else:
                print("Out of range.")
        elif meal_group == "B":
            if 0 < int(meal_num) and int(meal_num) <= len(COMBO_B_COST):
                cost = COMBO_B_COST[int(meal_num) - 1]
                costed = round(cost, 2)
                print("$ {:.2f}".format(costed))
                print(meal_id)
                total_cost += costed
                setdone = True  
            else:
                print("Out of range.")
        else:
            print("Invalid.")

    add = input("Do you want to add any additional meal ids? Press 'y' for yes, 'n' for no: ")
    if add.lower() != 'y':
        print("Total cost:", total_cost)
        break

