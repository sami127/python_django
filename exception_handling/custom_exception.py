class Error(Exception):
    pass

class valueTooSamallError(Error):
    pass

class valueTooLargeError(Error):
    pass

number = 10
while True:
    try:
        i = int(input("Enter a number : "))
        if i<number:
            raise valueTooSamallError
        elif i>number:
            raise valueTooLargeError
        else:
            break
    except valueTooLargeError:
        print("This value is too large")
    except valueTooSamallError:
        print("This value is too small")
    except Exception as e:
        print("some other error occure ", e)
    
print("You guessed it correctly")