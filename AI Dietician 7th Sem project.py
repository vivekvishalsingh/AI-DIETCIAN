from tkinter import *
from random import randint

top = Tk()
top.config(bg='yellow')
top.title('The dietician')


def BMR():
    protein = ['Yogurt(1 cup)', 'Cooked meat(3 Oz)', 'Cooked fish(4 Oz)', '1 whole egg + 4 egg whites', 'Tofu(5 Oz)']
    fruit = ['Berries(80 Oz)', 'Apple', 'Orange', 'Banana', 'Dried Fruits(Handfull)', 'Fruit Juice(125ml)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)', 'Whole Grain Bread(1 slice)', 'Half Large Potato(75g)', 'Oats(250g)',
              '2 corn tortillas']
    ps = ['Soy nuts(i Oz)', 'Low fat milk(250ml)', 'Hummus(4 Tbsp)', 'Cottage cheese (125g)', 'Flavored yogurt(125g)']
    taste_en = ['2 TSP (10 ml) olive oil', '2 TBSP (30g) reduced-calorie salad dressin', '1/4 medium avocado',
                'Small handful of nuts', '1/2 ounce  grated Parmesan cheese',
                '1 TBSP (20g) jam, jelly, honey, syrup, sugar']

    w = v3.get()
    h = v4.get()
    age = v5.get()
    act = str(Lb.get(ACTIVE))
    gender = Lb2.get(ACTIVE)

    if gender == 'Male':
        cal = float()
        cal = 88.362 + (13.397 * float(w)) + (4.799 * float(h)) - (5.677 * float(age))
        print(cal)
    elif gender == 'Female':
        cal = float()
        cal = 447.593 + (9.247 * float(w)) + (3.098 * float(h)) - (4.330 * float(age))

    if act == 'Sedentary (little or no exercise)':
        cal = cal * 1.2

    elif act == 'Lightly active (1-3 days/week)':
        cal = cal * 1.375

    elif act == 'Moderately active (3-5 days/week)':
        cal = cal * 1.55

    elif act == 'Very active (6-7 days/week)':
        cal = cal * 1.725

    elif act == 'Super active (twice/day)':
        cal = cal * 1.9

    print(cal)

    if cal < 1500:
        fin = StringVar()
        fin = "Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)]
        label.config(text=fin)

        fin2 = StringVar()
        fin2 = "Lunch: " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + taste_en[randint(0, 5)]
        label2.config(text=fin2)

        fin3 = StringVar()
        fin3 = "Snack: " + ps[randint(0, 4)] + " + " + vegetable[0]
        label3.config(text=fin3)

        fin4 = StringVar()
        fin4 = ("Dinner: " + protein[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + taste_en[randint(0, 5)])
        label.config(text=fin4)

        fin5 = StringVar()
        fin5 = ("Snack: " + fruit[randint(0, 5)])
        label5.config(text=fin5)

    elif cal < 1800:
        fin = IntVar()
        fin = ("Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        label.config(text=fin)

        fin2 = StringVar()
        fin2 = ("Lunch: " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        label2.config(text=fin2)

        fin3 = StringVar()
        fin3 = ("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
        label3.config(text=fin3)

        fin4 = StringVar()
        fin4 = ("Dinner: 2 " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + taste_en[randint(0, 5)])
        label4.config(text=fin4)

        fin5 = StringVar()
        fin5 = ("Snack: " + fruit[randint(0, 5)])
        label5.config(text=fin5)

    elif cal < 2200:
        fin = StringVar()
        fin = ("Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        label.config(text=fin)

        fin2 = StringVar()
        fin2 = ("Lunch: " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        label2.config(text=fin2)

        fin3 = StringVar()
        fin3 = ("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
        label3.config(text=fin3)

        fin4 = StringVar()
        fin4 = ("Dinner: 2 " + protein[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + taste_en[randint(0, 5)])
        label4.config(text=fin4)

        fin5 = StringVar()
        fin5 = ("Snack: " + fruit[randint(0, 5)])
        label5.config(text=fin5)

    elif cal >= 2200:
        fin = StringVar()
        fin = ("Breakfast: 2 " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)] + " + " + grains[randint(0, 4)])
        label.config(text=fin)

        fin2 = StringVar()
        fin2 = ("Lunch: " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        label2.config(text=fin2)

        fin3 = StringVar()
        fin3 = ("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
        label3.config(text=fin3)

        fin4 = StringVar()
        fin4 = ("Dinner: 2 " + protein[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens + 2 " + grains[
            randint(0, 4)] + " + 2 " + taste_en[randint(0, 5)])
        label4.config(text=fin4)

        fin5 = StringVar()
        fin5 = ("Snack: " + fruit[randint(0, 5)])
        label5.config(text=fin5)


C = Canvas(top, bg="blue", height=100, width=1024, highlightthickness=5, highlightbackground="black")
C.pack()

C2 = Canvas(top, bg="powder blue", height=800, width=1024, highlightthickness=5, highlightbackground="black")
C2.pack()

l = Label(top, text='The Dietician', bg='yellow', relief='raised', borderwidth=5)
l.config(font=('helvetica', 50))
C.create_window(512, 50, window=l)

v3 = StringVar()
v4 = StringVar()
v5 = StringVar()

Lb2 = Listbox(top, bd=5, width=25, height=3)
Lb2.insert(1, 'Male')
Lb2.insert(2, 'Female')
C2.create_window(611, 240, window=Lb2)

Lb = Listbox(top, bd=5, height=5, width=55)
Lb.insert(1, 'Sedentary (little or no exercise)')
Lb.insert(2, 'Lightly active (1-3 days/week)')
Lb.insert(3, 'Moderately active (3-5 days/week)')
Lb.insert(4, 'Very active (6-7 days/week)')
Lb.insert(5, 'Super active (twice/day)')
C2.create_window(522, 315, window=Lb)
var = Lb.get(ACTIVE)
print(var)

l2 = Label(top, text="Weight", height=2, width=15, borderwidth=5, relief="raised")
l2.config(font=('italic', 15))
C2.create_window(440, 60, window=l2)

e3 = Entry(top, text="number", textvariable=v3, bd=5, width=7, font=('helvetica', 30))
C2.create_window(611, 60, window=e3)

l4 = Label(top, text="Height(in cms)", height=2, width=15, borderwidth=5, relief="raised")
l4.config(font=('italic', 15))
C2.create_window(440, 120, window=l4)

e4 = Entry(top, text="number", textvariable=v4, bd=5, width=7, font=('helvetica', 30))
C2.create_window(611, 120, window=e4)

l5 = Label(top, text="Age", height=2, width=15, borderwidth=5, relief="raised")
l5.config(font=('italic', 15))
C2.create_window(440, 180, window=l5)

e5 = Entry(top, text="number", textvariable=v5, bd=5, width=7, font=('helvetica', 30))
C2.create_window(611, 180, window=e5)

l6 = Label(top, text="Gender", height=2, width=15, borderwidth=5, relief="raised")
l6.config(font=('italic', 15))
C2.create_window(440, 240, window=l6)

label = Label(top, bg="blue")
label.config(font=('Italic 14 bold'))
C2.create_window(512, 430, window=label)

label2 = Label(top, bg="blue")
label2.config(font=('Italic 14 bold'))
C2.create_window(512, 460, window=label2)

label3 = Label(top, bg="blue")
label3.config(font=('Italic 14 bold'))
C2.create_window(512, 490, window=label3)

label4 = Label(top, bg="blue")
label4.config(font=('Italic 14 bold'))
C2.create_window(512, 520, window=label4)

label5 = Label(top, bg="blue")
label5.config(font=('Italic 14 bold'))
C2.create_window(512, 550, window=label5)

button = Button(top, text=" Submit ", bd=5, bg="red", fg="black", height=2, width=8, command=BMR)
C2.create_window(512, 385, window=button)

top.mainloop()