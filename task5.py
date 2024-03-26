#Finances

def budget_info():
    income=int(input("How much income this month? "))
    expense=int(input("How much money you spend this month? "))
    return income, expense

def calculate_budget(income, expense):
    budget=income-expense
    return budget



inc, out=budget_info()
remaining_budget=calculate_budget(inc, out )
print("Your remaining budget is: ", remaining_budget, "AZN")
   

#Body&Health

def body_propotions():
    weight=float(input('Please enter your weight in kilograms: '))
    height=float(input("Please enter your height in meters: "))

    res=bmi_index(weight, height)
    category=bmi_standarts(res)

    print("Your bmi is", res, "which means: ", category)

    
def bmi_index(weight, height):
    bmi=weight/(height/100)**2
    return bmi


def bmi_standarts(bmi):
    if bmi<18.5:
     return "You BMI index is weak" 
    elif bmi>18.5 and bmi<=25:
       return "Your BMI index is normal"
    elif bmi>25 and bmi<=30:
       return "You're well-fed"
    else:
       return "Warning! You're overweight"



start=body_propotions()
print(start)



#Education

def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

   
def evaluate_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"


def collect():
    scores = []
    subjects = ["algebra", "geometry", "chemistry", "geography", "biology"]
    for subject in subjects:
        score = float(input(f"Enter the score for {subject.capitalize()}: "))
        scores.append(score)
    
    average_score = calculate_average(scores)
    grade = evaluate_grade(average_score)
    print(f"Your average score: {average_score}")
    print(f"Grade: {grade}")

collect()
