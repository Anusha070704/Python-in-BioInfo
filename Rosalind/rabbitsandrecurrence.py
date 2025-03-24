def Fibonacci_Loop_Pythonic(months,offsprings):
    parent,child=1,1
    for itr in range(months-1):
        child,parent=parent,parent+(child*offsprings)
    return child

def Wascally_Wabbits(month,offspringCount):
    if month==1:
        return 1
    elif month==2:
        return offspringCount
    oneGen=Wascally_Wabbits(month-1,offspringCount)
    twoGen=Wascally_Wabbits(month-2,offspringCount)
    if month<=4:
        return(oneGen+twoGen)
    return(oneGen+(twoGen*offspringCount))
print(Fibonacci_Loop_Pythonic(35,2))


