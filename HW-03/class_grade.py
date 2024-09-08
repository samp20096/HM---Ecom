# start

grade: int = int(input("What grade you received? "))

match grade:
    case grade if 0 <= grade <= 40:
        print("Try harder next time")
    case grade if 21 <= grade <= 60:
        print("You're getting there, need some work")
    case grade if 61 <= grade <= 80:
        print("Pretty good")
    case grade if 81 <= grade <= 95:
        print("Awesome!")
    case rade if 96 <= grade <= 100:
        print("Excellent! you're a Star!!")
    case _:
        print("Illegal Grade!")

# End