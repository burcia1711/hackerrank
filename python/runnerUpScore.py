if __name__ == '__main__':
    student_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_scores.append([name, score])

second_highest = sorted(set([score for name, score in student_scores]))[1]
print('\n'.join(sorted([name for name, score in student_scores if score == second_highest])))
