# Match-case statemet (switch): An alternative to using many 'elif statements
#                               Execute some code if a value matches a 'case
#                               Benefits: cleaner and syntax is more readable

def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return "Not a valid day"
        
print(is_weekend("Sunday"))
