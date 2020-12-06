# coding=gbk
import math
from collections import Counter

positive = ['好吃', '好', '不错', '好评', '不错', '辛苦', '赞', '喜欢', '棒']
negtive = ['难吃', '差评', '迟到', '扔', '不', '太慢', '少', '差', '慢', '晚', '垃圾', '失望', '恶心']

sents = [[]]
counter = Counter()
total = 0


def calc_scores(_sents, _counter, _total):
    global sents, counter, total
    sents = _sents
    counter = _counter
    total = _total

    scores = dict()
    progress = 0

    for word in counter.keys():
        if word in positive or word in negtive:
            continue
        scores[word] = SO_PMI(word)

        progress += 1
        if progress % int(len(counter) / 20) == 0:
            print('progress', '%.2f%%' % (progress / len(counter) * 100))

    return scores


def joint_count(w1):
    count_pos = [0] * len(positive)
    count_neg = [0] * len(negtive)

    for sent in sents:
        if w1 in sent:
            for i in range(len(positive)):
                if positive[i] in sent:
                    count_pos[i] += 1

            for i in range(len(negtive)):
                if negtive[i] in sent:
                    count_neg[i] += 1
    return count_pos, count_neg


def SO_PMI(w):
    score = 0
    count_pos, count_neg = joint_count(w)
    for i in range(len(positive)):
        score += math.log((count_pos[i] * total + 1) / (counter[w] * counter[positive[i]] + 1), 2)

    for i in range(len(negtive)):
        score -= math.log((count_neg[i] * total + 1) / (counter[w] * counter[negtive[i]] + 1), 2)

    return score
