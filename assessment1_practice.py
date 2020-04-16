def question_first_solution(length, breadth):
    if length == breadth:
        return length * breadth, True
    else:
        return length * breadth, False

    pass
print (question_first_solution(5,5))

def question_second_solution(nums):
    nums = "5"
    if (nums.isdigit()):
        n = int(nums)
        nn = str(n) + str(n)
        nnn = str(n) + str(n) + str(n)
        return n + int(nn) + int(nnn)
    else:
        return "No is not an integer no"
print(question_second_solution(5))

def question_third_solution(sal, noy):
    if noy <=5:
        pf = sal * 12 / 100
    elif noy >=5:
        pf = sal * 24 / 100
    return sal - pf
    pass
print(question_third_solution(25000,5))

def question_fourth_solution(a, b, c, d, e):
    total_marks = a + b + c + d + e
    per_of_marks = total_marks / 500 * 100

    if per_of_marks > 90 and per_of_marks <= 100:  # for failsafe i have used this is if grade is higher than 100 then it will show error
        grade = "A+"
    elif per_of_marks >= 80 and per_of_marks <= 90:
        grade = "A"
    elif per_of_marks >= 70 and per_of_marks <= 80:
        grade = "B+"
    elif per_of_marks >= 60 and per_of_marks <= 70:
        grade = "B"
    elif per_of_marks >= 50 and per_of_marks <= 60:
        grade = "C+"
    elif per_of_marks >= 40 and per_of_marks <= 50:
        grade = "C"
    elif per_of_marks < 40:
        grade = "F"
    else:
        grade = "error in grade"
    return grade, per_of_marks
    pass

print(question_fourth_solution(50,96,85,65,95))

def question_fifth_solution(noc,n):
    per_of_attendance = n / noc * 100
    attendance = format(per_of_attendance, '.2f') #just for formating the output in 2 decimal
    if per_of_attendance < 75:
        allow = False
    else:
        allow = True
    return attendance, allow
    pass
print(question_fifth_solution(248,189))


def question_sixth_solution(year):
    if (year % 4) == 0 or (year % 4) == 0:
        leap = True
    else:
        leap = False
    return leap
    pass
print(question_sixth_solution(2020))

def question_seventh_solution(age, gen , mar_status):
    #age = 25, gen = F, mar_status = Y
    if gen == "F" and age ==() and mar_status == ():
        place_of_service = "You will work only in urban areas"
    elif gen == "M" and (age >=20 and age <=30) and mar_status == "N":
        place_of_service = "You may work anywhere"
    elif gen == "F" and (age >= 20 and age <= 30) and mar_status == "N":
        place_of_service = "You may work in urban areas"
    elif gen == "M" and (age >=20 and age <=30) and mar_status == "Y":
        place_of_service = "You will work in nearby Hometown"
    elif gen == "F" and (age >=20 and age <=30) and mar_status == "Y":
        place_of_service = "You will work in your husband's city."
    elif age <=20 or age >=30:
        place_of_service = "ERROR"
    else:
        place_of_service  = "Invalid Input"
    return place_of_service
    pass
print(question_seventh_solution(25,"F","Y"))

def question_eighth_solution(x,y,z):
    if x == y == z:
        type_of_triangle = "Equilateral Triangle"
    elif x==y or y == z or x == z:
        type_of_triangle = "Isosceles"
    else:
        type_of_triangle = "Scalene "
    return type_of_triangle
    pass
print(question_eighth_solution(5,6,5))


'''9. A shop will give a discount of 10% max upto 150rs if the cost of the purchased quantity is more than 1000.
Enter quantity Suppose, one unit will cost 100rs. Judge and print total cost for the customer.
'''
def question_ninth_solution(n):
    # n = 15
    cost_per_unit = 100
    max_discount = 150
    cost_of_purchased = n * cost_per_unit # 15 * 100  = 1500
    # print("Purchased cost " + str(cost_of_purchased))

    if cost_of_purchased > 1000:
        apply_discount = 10 * cost_of_purchased / 100
        # print("apply_discount " + str(apply_discount))
        if apply_discount >= 150:
            apply_discount == 150
            # print(apply_discount)
            # return new_discount
            total_bill = cost_of_purchased - apply_discount
            # print(total_bill)
            return total_bill
        else:
            print("Purchased more to get 10% or Max Rs. 150 as a discount")
    else:
        print("Purchased more to get 10% or Max Rs. 150 as a discount")


print(question_ninth_solution(1))
'''
# we need to import datetime module to directly get the diffrence between dates and we aloso need the input in
from datetime import date
def question_tenth_solution(a,b):
    a_split = a.split("/") # first split the input into the parts
    # print(a_split)
    a = date(int(a_split[2]),int(a_split[1]),int(a_split[0])) #convent it into date format
    # print (a)
    # print(type(a))
    b_split = b.split("/")
    b = date(int(b_split[2]),int(b_split[1]),int(b_split[0]))
    days_diff = (b - a).days
    return days_diff
'1 days 0 months 0 years'

print(question_tenth_solution("25/01/2020", "26/01/2020"))




