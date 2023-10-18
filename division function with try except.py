def div42by(divBy):
    try:
        return 42 / divBy
    #except doesn't always require an error - if you type it in without the error code, it catches anything
    except ZeroDivisionError: 
        print ('Division by Zero error.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))