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
    # vocab_test(words_by_author)
    # jaccard_test(words_by_author, len_shortest_corpus)
    

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
    plt.show(block=True)

if __name__ == "__main__":
    main()
    