# assert condion, message

def avg(marks):
    assert len(marks) != 0, "Hi there exucution stopped here"
    return sum(marks)/len(marks)

mark1 = []
print("Average of mark1:",avg(mark1))
