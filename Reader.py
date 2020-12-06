# coding=utf-8
from collections import Counter

import jieba

punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒~ ^ω★╮╯▽๑ ั ็ω ็ ั๑o^^o♪#↖^ω^↗
﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')


def read(path):
    sents = []
    counter = Counter()
    total = 0

    with open(path, encoding='utf-8') as file, open('output_pos.txt', 'w+', encoding='utf-8') as out_pos, \
            open('output_neg.txt', 'w+', encoding='utf-8') as  out_neg:
        file.readline()
        for line in file:
            words = jieba.lcut(line[2:])
            words = [w for w in words if w not in punct]

            sents.append(words)
            counter.update(words)
            total += len(words)

            if line[0] == '1':
                out_pos.write(' '.join(words))
                out_pos.write('\n')
            else:
                out_neg.write(' '.join(words))
                out_neg.write('\n')

    i = 0
    for name, num in counter.most_common(300):
        i += 1
        print(i, name, num)

    print(total)

    return sents, counter, total


if __name__ == '__main__':
    read('comments.csv')
