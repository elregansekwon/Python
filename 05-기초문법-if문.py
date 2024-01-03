#input()함수 : 입력 값을 받음
#input함수는 입력 값 받을 때 그냥 무조건 문자열로 받아들인다.
#input 함수 안에 ""쓰고 안에 띄우고 싶은 말 쓰기
score = int(input("점수 입력 >> ")) # int() : 문자열형 --> 정수형
if score >= 90: #if 조건 쓰고 밑에 내려서 한 번 들여써서 출력 값
    print("학점 : A")
elif 80 <= score < 90: #elif : 그게 아니라면
    print("학점 : B")
elif 70 <= score < 80:
    print("학점 : C")
else: #else : 위의 경우가 모두 아니라면
    print("학점 : F")
