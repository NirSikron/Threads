import random

# יוצר את הדיסק וה-RAM
Disk = [None] * 30
RAM = [None] * 15

# ממלא את הדיסק בערכים אקראיים
def fillDisk(Disk):
    for i in range(len(Disk)):
        Disk[i] = random.randint(0, 1000)
    print("\nDisk filled with random values:")
    print(Disk)

# מעביר ערכים רנדומליים מהדיסק ל-RAM
def moveToRam(Disk, RAM):
    for i in range(len(RAM)):
        while True:
            random_index = random.randint(0, len(Disk) - 1)
            if Disk[random_index] is not None:
                RAM[i] = Disk[random_index]
                Disk[random_index] = None
                break
    print("\nValues moved to RAM:")
    print("RAM:", RAM)
    print("Disk after moving values:", Disk)

# בודק אם ערך קיים ב-RAM
def isValid(value):
    result = value in RAM
    print(f"\nChecking if value {value} is in RAM:")
    print(f"Result: {result}")
    return result

# מחזיר ערך לדיסק אם אינו קיים ב-RAM
def isDirty(value):
    print(f"\nChecking if value {value} is dirty (not in RAM):")
    if not isValid(value):
        for i in range(len(Disk)):
            if Disk[i] is None:
                Disk[i] = value
                print(f"Value {value} added to Disk at index {i}.")
                break
    else:
        print(f"Value {value} is already valid in RAM.")

# מעדכן ערכים ב-RAM ובודק מול הדיסק
def is_diry(RAM, Disk):
    random_index = random.randint(0, len(RAM) - 1)
    val = random.randint(0, 1000)
    print(f"\nUpdating RAM at index {random_index} with value {val}.")
    RAM[random_index] = val
    if val not in Disk:
        for i in range(len(Disk)):
            if Disk[i] is None:
                Disk[i] = val
                print(f"Value {val} added to Disk at index {i}.")
                break

# בדיקת הרשאות
def is_p(value, RAM):
    print(f"\nChecking permissions with value {value}:")
    if value == 1:
        accessible_values = RAM[:5]
        print(f"\u2705 Access granted. Values in RAM (up to index 5): {accessible_values}")
        return accessible_values
    elif value == 0:
        print("\u26d4 Access denied. Please contact your admin.")
        return None
    else:
        print("\u26a0 Invalid permission value. Use 1 for high or 0 for low permissions.")
        return None

# פונקציה ליצירת מערך מונים
def counterArray(Disk, array):
    print("\nGenerating counters array:")
    counter = 0
    size = 10
    my_array = [0] * size
    for i in range(size):
        my_array[i] = random.randint(0, 1000)
        if my_array[i] == 0:
            my_array[i] = -1
            counter += 1
    print("Generated counters array:", my_array)
    print("Number of updates (0 to -1):", counter)
    return my_array, counter

# פונקציה לניהול מחסנית ומערך מונים
def update_counters(stack, counters, max_value=10):
    """
    מנהל מחסנית ומערך מונים:
    - מוסיף ערך למחסנית ומעדכן את מערך המונים.
    - בודק אם יש ערכים במערך המונים שמונם שווה ל-0,
      ואם הם קיימים במחסנית, מחליף את המונה שלהם ל--1.
    - בסיום, מחליף כל ערך שנשאר 0 ל--1.
    """
    # שלב 1: הוספת ערך חדש למחסנית ועדכון המונה
    new_value = random.randint(0, max_value - 1)
    stack.append(new_value)
    counters[new_value] += 1
    print(f"\nAdded value {new_value} to stack.")
    print(f"Stack after addition: {stack}")
    print(f"Counters after addition: {counters}")

    # שלב 2: בדיקה של ערכים במערך המונים עם מונה 0
    for i in range(len(counters)):
        if counters[i] == 0 and i in stack:  # אם המונה שווה ל-0 והערך קיים במחסנית
            counters[i] = 1  # עדכון המונה ל-1 (רק עבור ערכים במחסנית)
            print(f"Value at index {i} in counters was 0 and exists in stack. Updated to 1.")

    # שלב 3: החלפת כל הערכים שנשארו 0 ל--1
    for i in range(len(counters)):
        if counters[i] == 0:  # אם המונה נשאר 0
            counters[i] = -1  # מעדכן אותו ל--1
            print(f"Value at index {i} in counters remained 0. Updated to -1.")

    # הדפסה סופית לאחר הבדיקה
    print(f"Counters after final update: {counters}")
    return stack, counters

# קריאה לפונקציות
fillDisk(Disk)
moveToRam(Disk, RAM)
value = random.randint(0, 1000)
isDirty(value)
is_diry(RAM, Disk)

stack = []
counters = [0] * 10
for _ in range(3):
    stack, counters = update_counters(stack, counters)

# הצגת מצב סופי
print("\nFinal stack:", stack)
print("Final counters array:", counters)

# קריאה לפונקציה is_p
permission_value = random.randint(0, 1)  # הרשאות אקראיות (0 או 1)
accessible_data = is_p(permission_value, RAM)

# הצגת נתונים שניתן לגשת אליהם
if accessible_data is not None:
    print(f"Accessible data in RAM: {accessible_data}")
else:
    print("No data accessible due to insufficient permissions.")
