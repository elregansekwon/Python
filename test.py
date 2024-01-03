from kiwipiepy import Kiwi

kiwi = Kiwi()
token_list = kiwi.tokenize("오늘 점심은 뭐 먹지?")
for i in token_list:
    print(i)