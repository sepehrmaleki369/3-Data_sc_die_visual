import pygal
from die import Die

die_1 = Die(20)
die_2 = Die(20)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

# calculating iteration of each number
for value in range(2, max_result+1):

    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


hist = pygal.Bar()

# automatic x label production
xLablesList = []
for i in range(2, max_result+1):
    xLablesList.append(str(i))


hist.title = "Results of rolling two D6  50000 times"
hist.x_labels =xLablesList
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add( 'D6 + D6', frequencies)
hist.render_to_file('die_visual-15-6.svg')