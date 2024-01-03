#While 조건부 반복문
# -->While을 쓰면 인터프리터가 While문 끝까지 갔다가 다시 While문 처음으로 돌아온다.
while True: # 무한 루프
    foo = input("문자열 입력 >> ")
    if foo == "종료":
        break # While 반복문 강제 탈출
    elif foo == "":
        print("다시 입력하세요!")
        continue # 반복문 처음으로 돌려보내기
    print(f"글자 수는 {len(foo)}개 입니다.")
    #print할 때 값을 출력되는 문장 안에 넣고 싶다면 문장 앞에 f쓰고 문장에는 {}쓰고 들어갔으면 좋겠는 변수 집어넣기.
