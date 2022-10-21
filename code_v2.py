import csv
input=open("test-input-1.csv")
file=csv.reader(input)
rows = []
for row in file:
    rows.append(row)
rooms=rows.pop(-1)
subjects_timeslots={}
subjects_optional={}

#Create dictionaries subjects_timeslots,subjects_optional
for row in rows:
    row=[element.strip() for element in row]
    subjects_timeslots[row[0]]=row[2:]
    subjects_optional[row[0]]=True if row[1]=="o" else False
timeslot_subject={}

#create timeslot_subject
for subject in subjects_timeslots:
    for timeslot in subjects_timeslots[subject]:
        if timeslot in timeslot_subject:
            timeslot_subject[timeslot].append(subject)
        else:
            timeslot_subject[timeslot]=[subject]


print(timeslot_subject)