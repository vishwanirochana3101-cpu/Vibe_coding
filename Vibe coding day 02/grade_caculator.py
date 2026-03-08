while True:
    print("\n" + "="*30)
    print("      GRADE CALCULATOR")
    print("="*30)
    
    name = input("Enter student's name (or type 'Exit' to stop): ")
    
    if name.lower() == 'exit':
        print("\nExiting the program. Goodbye!")
        break
    
    # ලකුණු ලබා ගැනීම
    mark1 = int(input("Enter Mark 1: "))
    mark2 = int(input("Enter Mark 2: "))
    mark3 = int(input("Enter Mark 3: "))

    # සාමාන්‍යය ගණනය කිරීම
    average = (mark1 + mark2 + mark3) / 3

    # ශ්‍රේණිය තීරණය කිරීම
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # පිරිසිදු සහ ලස්සන ප්‍රතිඵලය (Formatted Output)
    print("\n------------------------------")
    print(f"Name    : {name}")
    print(f"Average : {average:.1f}") # එක දශමස්ථානයකට පෙන්වීමට
    print(f"Grade   : {grade}")
    print("------------------------------")
