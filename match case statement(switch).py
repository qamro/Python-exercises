# match case statement(switch) in python
# the match case statement is a more readable way to write if-elif-else chains
# the format is: match variable:
#                 case value:
#                     # do something
#                 case _:
#                     # do something else


# an example of using match case statement to determine the day of the week
def day_of_week(day):
    match day:
        case 1:
            return "It's Sunday, the start of the week."
        case 2:
            return "It's Monday, the second day of the week."
        case 3:
            return "It's Tuesday, the third day of the week."
        case 4:
            return "It's Wednesday, the middle of the week."
        case 5:
            return "It's Thursday, almost the weekend."
        case 6:
            return "It's Friday, time to relax!."
        case 7:
            return "It's Saturday, time to prepare for the week ahead."
        case _:
            return "That's not a valid day of the week."
        
        
print(day_of_week(1))
print(day_of_week(4))
print(day_of_week(7))
print(day_of_week(8))
print(day_of_week("Message"))