#introduction
print("This is calculator of callories and BMI")

#Choose
player=input("Choose type of operation (callories/BMI)")

#calories
while True:
    if player == "callories":
        player1=input("Enter your sex (famele/male)")
        if player1 == "male":
            weight=float(input("Write your weight (kg)"))
            height=float(input("Write your height (сm)"))
            age=float(input("Write your age(years)"))
            result1=float(10*weight)
            result2=float(6.25*height)
            result3=float(4.92*age)
            result4=float(result1+result2-result3-5)
            print(f"You need eat {result4} calories every day" )
            player=input("Choose type of operation (callories/BMI)")

    
        elif player1 == "famele":
            weight=float(input("Enter your weight (kg)"))
            height=float(input("Enter your height (Cm)"))
            age=float(input("Enter your age(years)"))
            result1=float((10*weight))
            result2=float(6.25*height)
            result3=float((4.92*age))
            result4=float((result1+result2-result3-161))
            print(f"You need eat {result4} calories every day")
            player=input("Choose type of operation (callories/BMI)")

        else:
            print("system:Somthing is wrong!Try again!")
            player1=input()

        
        
#BMI
     
    elif player == "BMI":
        weight=float(input("Enter your weight (kg)"))
        height=float(input("Enter your height(Exemple: 165 = 1.65)"))
        result1=float((height**2))
        result2=float((weight/result1))
        print(result2)
        print("""Interpretation of results:"  
less than 18.5 — lack of body weight
18-24,9 — normal
25-29.9 — overweight
30-34.9 — grade I obesity
35-39.9 — grade II obesity
40 and over — grade III obesity.""")
        player=input("Choose type of operation (callories/BMI)")
    
    else:
        print("system:Somthing is wrong!Try again!")
        player=input()

        

