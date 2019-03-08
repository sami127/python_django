import sys
random_list = ['a',0,2]
for e in random_list:
    try:
        print("the enty is ", e)
        r = 1/int(e)
        print("Result value is ",r)
    except ZeroDivisionError as e:
        print("You got exception here :ZeroDivisionError",sys.exc_info()) 
        print("Coming from exception class : ",e)
    except ValueError as e:
        print("You got exception here :ValueError",sys.exc_info()) 
        print("Coming from exception class : ",e)    
    except Exception as e:
        print("You got exception here :",sys.exc_info()) 
        print("Coming from exception class : ",e)    
    finally:
        print("I am inside finally block")

# "0" -> int("0") ->0
# "0" -> float("0") ->0.0
# 0 -> str(0) ->"0"
Exception

