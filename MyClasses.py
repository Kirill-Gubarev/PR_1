class Session:  # класс сессия
    __semester = -1  # семестр
    __countTests = -1  # количество зачетов
    __countPassedTests = -1  # количество сданных зачетов
    __countExams = -1  # количество экзаменов
    __countPassedExams = -1  # количество сданных экзаменов

    def __init__(self, semester, countExams):  # инициализация экземпляра
        if semester < 1:  # если семестр меньше 1
            self.__semester = 1  # присвоить 1
        elif semester > 8:  # если семестр больше 8
            self.__semester = 8  # присвоить 8
        else:  # если семестр между 1 и 8
            self.__semester = semester  # присвоить semester

        if countExams > 4:  # если количество экзаменов больше 4
            self.__countExams = 4  # присвоить 4

        if semester == 3 or semester == 7:  # если семестр 3 или 7
            self.__countTests = 3  # присвоить 3
        elif semester == 5 or semester == 6:  # если семестр 5 или 6
            self.__countTests = 4  # присвоить 4
        else:  # если семестр  не 3 5 6 7
            self.__countTests = 5  # присвоить 5

        self.__countPassedTests = 0
        self.__countPassedExams = 0

    def isSetTest(self):  # можно ли поставить зачет
        return self.__countTests == self.__countPassedTests and self.__countExams == self.__countPassedExams  # сравнить количество всех и сданных зачетов и экзаменов и всернуть

    def addCountPassedTests(self):  # увеличить количество сданных зачетов на 1
        if self.__countPassedTests + 1 < self.__countTests:  # если количество сданных зачетов + 1 меньше чем количество зачетов
            self.__countPassedTests += 1  # увеличить количество сданных зачетов на 1
        return self  # вернуть ссылку на себя

    def addCountPassedExams(self, countPassedExams):  # увеличить количество сданных зкзаменов на 1
        if self.__countPassedExams + 1 < self.__countExams:  # если количество сданных экзаменов + 1 меньше чем количество экзаменов
            self.__countPassedExams += 1  # увеличить количество сданных зкзаменов на 1
        return self  # вернуть ссылку на себя

    def setCountPassedTests(self,countPassedTests):  # увеличить количество сданных зачетов
        if countPassedTests < self.__countTests:  # если количество сданных зачетов меньше чем количество зачетов
            self.__countPassedTests = countPassedTests  # установить количество сданных зачетов
        else:
            self.__countPassedTests = self.__countTests
        return self  # вернуть ссылку на себя

    def setCountPassedExams(self,countPassedExams):  # увеличить количество сданных зкзаменов
        if countPassedExams < self.__countExams:  # если количество сданных экзаменов меньше чем количество экзаменов
            self.__countPassedExams = countPassedExams  # установить количество сданных зкзаменов
        else:
            self.__countPassedExams = self.__countExams
        return self  # вернуть ссылку на себя

    def getSemester(self):  # получить семестр
        return self.__semester  # вернуть семестр

    def getCountTests(self):  # получить количество зачетов
        return self.__countTests  # вернуть количество зачетов

    def getCountPassedTests(self):  # получить количество сданных зачетов
        return self.__countPassedTests  # вернуть количество сданных зачетов

    def getCountExams(self):  # получить количество экзаменов
        return self.__countExams  # вернуть количество экзаменов

    def getCountPassedExams(self):  # получить количество сданных экзаменов
        return self.__countPassedExams  # вернуть количество сданных экзаменов


class SummerSession(Session):  # класс летняя сессия
    __assessmentForPractice = "-1"  # оценка за практику

    def setAssessmentForPractice(self, assessment):  # поставить оценку
        if (not self.isSetTest()):  # если сессия не сдана
            self.__assessmentForPractice = "н/а"  # присвоить не аттестован
        elif assessment == "н/а" or assessment == "зт" or assessment == "н/зт":  # если оценка соответствует н/а зт н/зт
            self.__assessmentForPractice = assessment  # присвоить оценку
        return self  # вернуть ссылку на себя

    def getAssessmentForPractice(self):
        return self.__assessmentForPractice  # вернуть оценку за практику
