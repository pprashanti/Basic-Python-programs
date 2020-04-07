score=int(input("enter the scores of the student"))
if score>=90:
    print("This student's score of " + str(score) + " is an A.")
else:
    if score>=80:
        print("This student's score of " + str(score) + " is an B.")
    else:
        if score>=70:
            print("This student's score of " + str(score) + " is an C.")
        else:
            if score>=60:
                print("This student's score of " + str(score) + " is an D.")
            else:
                print("This student's score of " + str(score) + " is an F.")


