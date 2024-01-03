#[]이 리스트
foo = [1, 2, 3, "Hello", [1,2,3]]
fruit = ["사과", "오렌지", "포도"]
#리스트 원소에 번호 매길 때 0,1,2,3 ... 순으로 매긴다.->원소를 인덱스라고 부르고 이 숫자를 인덱스 번호라고 부른다.
print(fruit[2]) #해당 문자열에서 꺼내고 싶은 원소의 인덱스 번호를 []안에 쓴다

fruit.append("수박") #append : 리스트에 원소 추가
print(fruit)

fruit.remove("오렌지") #remove : 리스트에 원소 삭제
print(fruit)

##주의
#remove와 append는 함수 적용의 결과 값을 뱉어내지X -> 따라서 바로 print를 씌우면 None으로 출력된다.

fruit.append("딸기")
print(len(fruit)) #len(리스트)를 하면 문자 원소의 개수가 나온다

#함수이름.sort() : 오름차순 정렬
fruit.sort(reverse=True) #리스트 원소 내림차순 정렬
#sort 함수도 print 따로 씌워야 한다.
print(fruit)

fruit[0] = "귤" #리스트 원소 값 수정