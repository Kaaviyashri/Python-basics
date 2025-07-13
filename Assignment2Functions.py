class Assignment2():
    def subfields():
            sub_fields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
            print("Sub-fields in AI are:")
            for field in sub_fields:
                print(field)
    
    
    def OddEven():
            num = int(input("Enter a number: "))
            if(num % 2 == 0):
                print(f"{num} is a even number")
            else:
                print(f"{num}is a odd number")
    
    def Eligible():
            gender = input("Your gender: ").lower()
            age = int(input("Your age: "))
            if(gender == "male" and age >= 21):
                print("Eligible")
            elif(gender == "female" and age >= 18):
                print("Eligible")
            else:
                print("Not Eligible")
    
    def percentage():
            subject1 = int(input("Subject1 = "))
            subject2 = int(input("Subject2 = "))
            subject3 = int(input("Subject3 = "))
            subject4 = int(input("Subject4 = "))
            subject5 = int(input("Subject5 = "))
            full_score = 500
            total = subject1 + subject2 + subject3 + subject4 + subject5
            print("Total = ", total)
            percent = total/full_score * 100
            print("Percentage = ", percent)
    
    def triangle():
            breadth = int(input("Breadth: "))
            height = int(input("Height: "))
            print("Area formula: (Breadth * Height) / 2")
            print("Area of Triangle: ", breadth * height / 2)
            height1 = int(input("Height1: "))
            height2 = int(input("Height2: "))
            breadth = int(input("Breadth: "))
            print("Perimeter formula: Height1+Height2+Breadth")
            print("Perimeter of Triangle:", height1 + height2 +breadth)