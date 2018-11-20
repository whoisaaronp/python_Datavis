import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []  # strip out the first row of test
installs = []
ratings = []


# open the csv file and parse it
with open("data/googleplaystore.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:  # strip the headers out
            print('pushing text row to categories array')
            categories.append(row)
            line_count += 1
        else:
            # collect the ratings info
            ratingsData = row[2]
            ratingsData = ratingsData.replace("NaN", "0")
            ratings.append(float(ratingsData))

            print('collect the rest of the data')
            installData = (row[5])
            installData = installData.replace(",", "")
            installData = installData.replace("Free", '0')
            installs.append(int(np.char.strip(installData, "+")))
            line_count += 1


print('processed', line_count, "rows of data")
print('first line:', ratings[0])
print('last line:', ratings[-1])


np_ratings = np.array(ratings)


popular_app = np_ratings > 4
pop_pct = int(len(np_ratings[popular_app]) / len(np_ratings) * 100)
print(pop_pct)


unpopular_app = np_ratings < 2
not_pop_pct = int(len(np_ratings[popular_app]) / len(np_ratings) * 100)
print(not_pop_pct)


mid_apps = 100 - (pop_pct + not_pop_pct)

# now we can plo stuff!!!
labels = "Sucks, Meh, LOVE IT!!"
sizes = [not_pop_pct, mid_apps, pop_pct]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Do We Loves Our Apps?")
plt.xlabel("User Rating - Google Play Store App Installs")
plt.show()
