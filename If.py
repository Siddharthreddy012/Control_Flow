person_1 = "ABC"
person_2 = "XYZ" 
interview={person_1 : True , person_2 : False}
if interview[person_1] :
    print("Welcome to IT Section")
else: 
    print("Go to cooking")
if interview[person_2] :
    print("Welcome to IT Section")
else: 
    print("Go to cooking")


siddu = {"Telugu": 85,"Hindi" : 70, "English" : 88, "Maths" : 75, "Science" : 95, "Social" :90}
print(siddu)
Marks = { siddu["Telugu"],siddu["Hindi"],siddu["English"],siddu["Maths"],siddu["Science"],siddu["Social"] }
print(Marks) 
qualify = set(range(35,101,1))
print(qualify)

if (Marks < qualify) :
    print("Pass")
else :
    print("Fail")


