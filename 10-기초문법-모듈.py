#모듈: 모듈을 import해오면 누군가 만들어 놓은 함수를 쓸 수 있다.
#파일 이름 지을 때 모듈 이름과 겹치지 않게 한다.->충돌 가능
#calendar은 내장모듈
#외장 모듈은 별도의 설치가 필요
import calendar as cal
#import 모듈명 as 모듈 별명 ->별명으로 모듈명을 단순화해서 쓸 수 있다.

#모듈명.  :함수 불러서 쓸 수 있다.
cal.prcal(2024)

#만약에 나는 함수 하나만 쓸 건데 모듈에서 함수를 전체 다 불러오는 것이 메모리적으로 손해?
#from 모듈명 import 함수명
#ex) from calendar import prcal
#그럼 모듈명. 안쓰고 바로 함수 이름만 불러서 prcal(2023)이렇게 쓸 수 있다.
