import sys
import os
import random
from collections import defaultdict, Counter

def main():
    message = input("Enter plaintext or ciphertext: ") 
    process = input("Enter 'encrypt' or 'decrypt': ")
    while process not in ('encrypt', 'decrypt'):
        process = input("Invalid process. Enter 'encrypt' or 'decrypt': ")
    shift = int(input("Shift value (1-366) = "))
    while not 1 <= shift <= 366:
        shift = int(input("Invalid value. Enter digit from 1 to 366: "))
    infile = input("Enter filename with extension: ")
    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile), file=sys.stderr)
        sys.exit(1)        
    text = load_file(infile) + '/' # 메시지 보내기 실행 시 allied_attack_plan.txt 파일에 lost.txt에 없는 문자 추가
    char_dict = make_dict(text, shift)
    
    if process == 'encrypt':
        ciphertext = encrypt(message, char_dict)
        
        # Run QC protocols and print results.
        """
         중복 코드가 있으면 에러를 발생시키는 함수인데 
         기존에 값이 1개 밖게 없는데 입력문자에서 2개 이상 있으면 
         무조건 에러이기 떄문에 일단 비활성화. 방법을 찾아야 할 듯
        """
        # if check_for_fail(ciphertext):
        #     print("\nProblem finding unique keys.", file=sys.stderr)
        #     print("Try again, change message, or change code book.\n",
        #           file=sys.stderr)
        #     sys.exit()

        print("\nCharacter and number of occurrences in char_dict: \n")      
        print("{: >10}{: >10}{: >10}".format('Character', 'Unicode', 'Count'))
        for key in sorted(char_dict.keys()):
            print('{:>10}{:>10}{:>10}'.format(repr(key)[1:-1], # repr를 따옴표를 포함한 문자를 가져오는데 따옴표 제거 목적으로 [1:-1] 범위 사용
                                              str(ord(key)), # ord 함수는 하나의 문자에 대응하는 유니코드 정수 반환
                                              len(char_dict[key])))
        print('\nNumber of distinct characters: {}'.format(len(char_dict)))
        print("Total number of characters: {:,}\n".format(len(text)))
        
        print("encrypted ciphertext = \n {}\n".format(ciphertext))
        
        # Check the encryption by decrypting the ciphertext.
        print("decrypted plaintext = ")  
        for i in ciphertext:
            print(text[i - shift], end='', flush=True)

    elif process == 'decrypt':
        plaintext = decrypt(message, text, shift)
        print("\ndecrypted plaintext = \n {}".format(plaintext))
        

def load_file(infile):
    """Read and return text file as a string of lowercase characters."""
    with open(infile) as f:
        loaded_string = f.read().lower()
    return loaded_string

def make_dict(text, shift):
    """Return dictionary of characters as keys and shifted indexes as values."""
    char_dict = defaultdict(list)
    for index, char in enumerate(text):
        char_dict[char].append(index + shift)
    return char_dict

def encrypt(message, char_dict):
    """Return list of indexes representing characters in a message."""
    encrypted = []
    for char in message.lower():
        if char == '/':
            print(char,char_dict[char])
        if len(char_dict[char]) > 1:
            index = random.choice(char_dict[char])
        elif len(char_dict[char]) == 1:  # Random.choice fails if only 1 choice.
            index = char_dict[char][0]
        elif len(char_dict[char]) == 0:
            print("\nCharacter {} not in dictionary.".format(char),
                  file=sys.stderr)
            continue      
        encrypted.append(index)
    return encrypted

def decrypt(message, text, shift):
    """Decrypt ciphertext list and return plaintext string."""
    plaintext = ''
    indexes = [s.replace(',', '').replace('[', '').replace(']', '')
               for s in message.split()] # 암호화 결과처럼 ciphertext는 반드시 공백으로 구분돼야함
    for i in indexes:
        plaintext += text[int(i) - shift]
    return plaintext

def check_for_fail(ciphertext):
    """Return True if ciphertext contains any duplicate keys."""
    check = [k for k, v in Counter(ciphertext).items() if v > 1]
    if len(check) > 0:
        return True

if __name__ == '__main__':
    # main()

    # 함수 개별 테스트
    # text = load_file("lost.txt")
    # c = make_dict('rhgfdgdfg/',70)
    # print(c)
    # text2 = load_file("allied_attack_plan.txt")
    # d = make_dict(text2,70)
    


    # allied_attack_plan.txt 파일 문자 비교
    # print(set(c) - set(d))
    # print(set(d) - set(c))



    # 실습 프로젝트 1
    text1 = load_file("lost.txt")
    d = make_dict(text1,70)
    m = {}
    for key,value in d.items():
        m.update({key:len(value)})

    import matplotlib.pyplot as plt

    plt.bar(*zip(*sorted(m.items(),key=lambda x:-x[1])))
    plt.show()
