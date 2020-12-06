import Reader
import SO_PMI

if __name__ == '__main__':
    sents, counter, total = Reader.read('comments.csv')
    scores = SO_PMI.calc_scores(sents, counter, total)
    scores = sorted(scores.items(), key=lambda kv: (kv[1], kv[0]))

    print('negative')
    for i in range(0, 50):
        print(scores[i])

    print('positive')
    for i in range(-1, -51, -1):
        print(scores[i])