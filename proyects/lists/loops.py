"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    new_score = [round(score) for score in student_scores]
    return new_score



def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    conta = 0
    for var in student_scores:
        if var < 41 :
            conta += 1
    return conta


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    new_student_score = [score for score in student_scores if score >= threshold]
    return new_student_score


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    rangee = (highest-40)/4
    lis_rang = [int(41 + rangee*num) for num in range(4)]
    return lis_rang


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    new=[]
    for index, name in enumerate(student_scores):
        new.append(f"{index+1}. {student_names[index]}: {name}")
    return new


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect = [[name, point] for name, point in student_info if point == 100]
    #TODO para probar json!!!
    if perfect == []:
        return []
    return (perfect[0])

a = round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])
b = count_failed_students([90,40,55,70,30,25,80,95,38,40])
c = above_threshold([90,40,55,70,30,68,70,75,83,96],75)
d = letter_grades(100)
e = student_ranking([82],['Betty'])
f = perfect_score([['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]])
