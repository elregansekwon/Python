from kiwipiepy import Kiwi

kiwi = Kiwi()
#def를 쓰면 내가 모듈을 만들 수 있다.
#모듈에 들어갈 코드들을 전체 선택해서 tap키 눌러야 모듈에 들어간다
def get_nouns_list(text):
    token_list = kiwi.tokenize(text) #각 품사별로 나눠서 알려줌
    nouns_list = []
    for i in token_list:
        if i.tag =="NNG" or i.tag == "NNP":   # 각 품사 궁금하면 kiwipiepy 깃허브 밑에 페이지 보면 설명 나와있음 / NNG:일반명사, NNP:고유명사
            nouns_list.append(i.form)
    #print(nouns_list)
    return nouns_list   # return으로 함수의 결괏값 돌려주기-->함수에서는 결괏값을 오직 return 명령어로만 돌려받을 수 있음
