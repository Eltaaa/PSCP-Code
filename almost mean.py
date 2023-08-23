""" AlmostMean """


def main(population):
    """ finding student who is closest to mean but not exceeding mean """
    idnumber = []
    score = []
    for _ in range(population):
        data = input().split()
        idnumber.append(data[0])
        score.append(float(data[1]))
    mean = sum(score) / population
    below_mean = max([i for i in score if i <= mean])

    print(idnumber[score.index(below_mean)], end="\t")
    print(below_mean)


main(int(input()))
