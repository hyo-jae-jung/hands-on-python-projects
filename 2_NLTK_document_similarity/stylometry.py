import nltk 
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

LINES = ['-',':','--']

def main():
    strings_by_author = dict()
    strings_by_author['doyle'] = text_to_string('hound.txt')
    strings_by_author['wells'] = text_to_string('war.txt')
    strings_by_author['unknown'] = text_to_string('lost.txt')

    words_by_author = make_word_dict(strings_by_author)
    len_shortest_corpus = find_shortest_corpus(words_by_author)

    word_length_test(words_by_author, len_shortest_corpus)
    stopwords_test(words_by_author, len_shortest_corpus)
    parts_of_speech_test(words_by_author, len_shortest_corpus)
    vocab_test(words_by_author)
    jaccard_test(words_by_author, len_shortest_corpus)
    dispersion_plot(words_by_author)

def text_to_string(filename):
    with open(filename, encoding='utf-8', errors='ignore') as infile:
        return infile.read()
    
def make_word_dict(strings_by_author):
    """작가별로 코퍼스를 단어로 토큰화한 딕셔너리를 반환한다."""
    words_by_author = dict()
    for author in strings_by_author:
        tokens = nltk.word_tokenize(strings_by_author[author])
        words_by_author[author] = ([token.lower() for token in tokens
                                    if token.isalpha()])
    return words_by_author
    

def find_shortest_corpus(words_by_author):
    """가장 잛은 코퍼스의 길이를 반환한다."""
    word_count = []
    for author in words_by_author:
        word_count.append(len(words_by_author[author]))
        print('\nNumber of words for {} = {}\n'.format(author, len(words_by_author[author])))
    len_shortest_corpus = min(word_count)
    print('length shortest corpus = {}\n'.format(len_shortest_corpus))
    return len_shortest_corpus


def word_length_test(words_by_author, len_shrtest_corpus):
    """작가별로 단어 길이별 빈도를 표시하는 도수 분포 그래프를 그린다. 가장 짧은 코퍼스에 맞춰 다른 코퍼스 길이를 줄인다."""
    by_author_length_freq_dist = dict()

    plt.figure(1)
    plt.ion()

    for i, author in enumerate(words_by_author):
        word_lengths = [len(word) for word in words_by_author[author][:len_shrtest_corpus]]
        by_author_length_freq_dist[author] = nltk.FreqDist(word_lengths)
        by_author_length_freq_dist[author].plot(15,
                                                linestyle=LINES[i],
                                                label=author,
                                                title='Word Length',
                                                cumulative=True)

    plt.figure(2)

    for i, author in enumerate(words_by_author):
        word_lengths = [len(word) for word in words_by_author[author][:len_shrtest_corpus]]
        by_author_length_freq_dist[author] = nltk.FreqDist(word_lengths)
        by_author_length_freq_dist[author].plot(15,
                                                linestyle=LINES[i],
                                                label=author,
                                                title='Word Length',
                                                cumulative=False)

        
    plt.legend()
    # plt.show(block=True)


def stopwords_test(words_by_author, len_shortest_corpus):
    """작가별 불용어 빈도 그래프를 그린다. 가장 짧은 코퍼스에 맞춰 다른 코퍼스 길이를 줄인다."""
    stopwords_by_author_freq_dist = dict()
    plt.figure(3)
    stop_words = set(stopwords.words('english')) # 속도 향상을 위해 집합 사용
    #print('Number of stopwords = {}\n'.format(len(stop_words)))
    #print('Stopwords = {}\n'.format(stop_words))

    for i, author in enumerate(words_by_author):
        stopwords_by_author = [word for word in words_by_author[author][:len_shortest_corpus] if word in stop_words]
        stopwords_by_author_freq_dist[author] = nltk.FreqDist(stopwords_by_author)
        stopwords_by_author_freq_dist[author].plot(50,
                                                   label=author,
                                                   linestyle=LINES[i],
                                                   title='50 Most Common Stopwords')
    plt.legend()
    # plt.show(block=True)


def parts_of_speech_test(words_by_author, len_shortest_corpus):
    """명사, 동사, 부사 등 작가의 품사 사용을 그래프로 그린다."""
    by_author_pos_freq_dist = dict()
    plt.figure(4)
    for i, author in enumerate(words_by_author):
        pos_by_author = [pos[1] for pos in nltk.pos_tag(words_by_author[author][:len_shortest_corpus])]
        by_author_pos_freq_dist[author] = nltk.FreqDist(pos_by_author)
        by_author_pos_freq_dist[author].plot(15,
                                             label=author,
                                             linestyle=LINES[i],
                                             title='Part of Speech')
    plt.legend()
    # plt.show(block=True)


def vocab_test(words_by_author):
    """카이제곱 검정 통계량을 사용해 작가가 사용한 어휘를 비교한다."""
    chisquared_by_author = dict()
    for author in words_by_author:
        if author != 'unknown':
            combined_corpus = (words_by_author[author] + words_by_author['unknown'])
            author_proportion = (len(words_by_author[author])/len(combined_corpus))
            combined_freq_dict = nltk.FreqDist(combined_corpus)
            most_common_words = list(combined_freq_dict.most_common(1000)) 
            """
            특징
                단어의 종류 다름

            해결 방법
                H0가 "unknown과 author가 같다."이니까 각 word별 비율도 같을거기 때문에 문제를 
                동질성 검정(Test of Homogeneity)에서 적합도 검정(goodness of fit)으로 변경
                (word by unknown+author)*proportion(author)을 E값으로,
                word by author를 O값으로 사용
                차이가 당연히 클 것으로 예상이 되지만 궁극적인 목적이 author별 비교이므로
                각 카이제곱 통계량의 크기로 비교. 작은 게 unknown에 가깝다고 판단.
            """
            chisquared = 0
            for word, combined_count in most_common_words:
                observed_count_author = words_by_author[author].count(word)
                expected_count_author = combined_count * author_proportion
                chisquared+=((observed_count_author - expected_count_author)**2 / expected_count_author)
                chisquared_by_author[author] = chisquared 
            print('Chi-squared for {} = {:.1f}'.format(author, chisquared))
    most_likely_author = min(chisquared_by_author, key=chisquared_by_author.get)
    print('Most-likely author by vocabulary is {}\n'.format(most_likely_author))


def jaccard_test(words_by_author, len_shortest_corpus):
    """
    작가가 파악된 두 코퍼스와 작자미상의 코퍼스 사이의 자카드 유사도를 계산한다.
    word count는 배제하고 word type으로만 판단.
    """
    jaccard_by_author = dict()
    unique_words_unknown = set(words_by_author['unknown'][:len_shortest_corpus])
    authors = (author for author in words_by_author if author != 'unknown')
    for author in authors:
        unique_words_author = set(words_by_author[author][:len_shortest_corpus])
        shared_words = unique_words_author.intersection(unique_words_unknown)
        jaccard_sim = (float(len(shared_words)/(len(unique_words_author)+len(unique_words_unknown) - len(shared_words))))

        jaccard_by_author[author] = jaccard_sim
        print('Jaccard Similarity for {} ={}'.format(author, jaccard_sim))
    most_likely_author = max(jaccard_by_author, key=jaccard_by_author.get)
    print('Most-likely author by similarity is {}'.format(most_likely_author))


if __name__ == "__main__":
    main()