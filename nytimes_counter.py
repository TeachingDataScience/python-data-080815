
# Import required libraries
import csv

# Start a counter and store the textfile in memory
gender_counter = {}
age_counter = {}

lines = csv.reader(open('nyt1.csv'))
lines.next()

# For each line, fill in the counters
for line in lines:
    age, gender, impressions, clicks, signed_in = line
    if str(gender) not in gender_counter:
        gender_counter[gender] = 0
    gender_counter[gender] += 1
    if str(age) not in age_counter:
        age_counter[age] = 0
    age_counter[age] += 1
    
print "Gender 0: ", gender_counter['0']
print "Gender 1: ", gender_counter['1']
print "Ages: "
print age_counter