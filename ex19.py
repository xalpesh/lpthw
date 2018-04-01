def cheese_and_cracker ( cheese_count, boxes_of_cracker):
    print(f"you have {cheese_count} cheeses !")
    print(f"you have {boxes_of_cracker} box off cracker")
    print("Man that's enough for a party!")
    print("Get a blanket! \n")

print("We can give function numbers directly")
cheese_and_cracker(10,20)

print("OR, We can use varaible from our script:")
amount_of_cheese = 10
amount_of_cracker = 50

cheese_and_cracker(amount_of_cheese,amount_of_cracker)

print("Even we can do math inside")
cheese_and_cracker(10+20,30+60)

print("and we can combine the two variable and math ")
cheese_and_cracker(amount_of_cheese + 20, amount_of_cracker+10)

