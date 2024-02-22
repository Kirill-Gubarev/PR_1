from MyClasses import Session, SummerSession

s1 = Session(2, 10)  # 2 семестр 10 экзаменов

print(str(s1.getSemester()) + " семестр")  # 2 семестр
print(str(s1.getCountTests()) + " зачетов")  # 5 зачетов
print(str(s1.getCountExams()) + " экзаменов")  # 4 экзамена
print(str(s1.getCountPassedTests()) + " сданных зачетов")  # 0 экзамена
print(str(s1.getCountPassedExams()) + " сданных экзаменов")  # 0 экзамена

print(str(s1.addCountPassedTests().getCountPassedTests()) + " сданных зачетов")  # 1 сданных зачетов

print(s1.isSetTest())  # False

print(str(s1.setCountPassedTests(500).getCountPassedTests()) + " сданных зачетов")  # 5 сданных зачетов
print(str(s1.setCountPassedExams(4).getCountPassedExams()) + " сданных зачетов")  # 4 сданных зачетов

print(s1.isSetTest())  # True



ss1 = SummerSession(5, 1)  # 5 семестр 1 экзамен

print(ss1.setAssessmentForPractice("зт").getAssessmentForPractice())#н/а

ss1.setCountPassedTests(500)
ss1.setCountPassedExams(500)

print(ss1.setAssessmentForPractice("зт").getAssessmentForPractice())#зт


