
age_total = 0
i = 0
age_input = float(input("Please enter age %i: " % (i + 1)))

while age_input != -1:
    if age_input < 0:
        print("Please enter a valid age or terminate with -1.")
        age_input = float(input("Please enter age %i: " % (i + 1)))
        continue
    i += 1
    age_total += age_input
    avg_age = age_total/i
    print("There are currently %i people with a total age of %0.2f and an average age of %0.2f." % (
        i, age_total, avg_age))
    age_input = float(input("Please enter age %i: " % (i+1)))
print("In total there are %i people with a total age of %0.2f and an average age of %0.2f." % (i, age_total, avg_age))