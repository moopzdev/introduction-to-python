# Student Grade Evaluation

try:
    # FIRST RUN
    # fw = open("score.txt", "w", encoding="utf-8")
    # while True:
    #     studentid = input(
    #         "Enter student ID (press 'q' for exit): ")
    #     if studentid == "q":
    #         break
    #     if studentid == "":
    #         raise Exception("Input is required")
    #     score = input("Enter the score of the student: ")
    #     fw.writelines(studentid+"\t\t\t" + score + "\n")
    # fw.close()

    # # UPDATING NEW DATA
    # fr = open("score.txt", "r", encoding="utf-8")
    # print(fr.read())
    # fr.close()
    # fa = open("score.txt", "a", encoding="utf-8")
    # while True:
    #     studentid = input(
    #         "Enter student ID (press 'q' for exit): ")
    #     if studentid == "q":
    #         break
    #     if studentid == "":
    #         raise Exception("Input is required")
    #     score = input("Enter the score of the student: ")
    #     fa.writelines(studentid+"\t\t\t" + score + "\n")
    # fa.close()

    # READING DATA AND EVALUATING GRADES
    fr = open("score.txt", "r", encoding="utf-8")
    fw = open("grades.txt", "w", encoding="utf-8")
    for line in fr.readlines():
        studentid = line[0:-4].strip()
        score = line[-4:].strip()
        # print("studentid:"+studentid+"\tscore:"+score+"\n")
        score = int(score)
        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        else:
            grade = "F"
        print("studentid:"+studentid+"\tscore:" +
              str(score)+"\tgrade:"+grade+"\n")
        fw.writelines("studentid:"+studentid+"\tscore:" +
                      str(score)+"\tgrade:"+grade+"\n")
    fr.close()
    fw.close()

except Exception as e:
    print(e)
