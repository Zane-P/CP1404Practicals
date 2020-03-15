import random


def main():

    def score_calculation(score):
        result = ""
        if score < 0 or score > 100:
            result = "Invalid score"
        elif score >= 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        else:
            result = "Bad"
        return result

    input_score = float(input("Enter score: "))
    print(input_score, score_calculation(input_score))

    random_score = float(random.randint(1, 100))
    print(random_score, score_calculation(random_score))


main()
