# 로또번호를 랜덤으로 뽑아주는 프로그램
import random

numbers = range(1,46)
# 마치 [1,2,3,...,45]과 비슷하다

# 6개의 숫자를 뽑아 출력해주는 프로그램 작성

# alt + shift + 위or아래 방향키 : 아래에 복사
# alt + 위or아래 방향키 : 한줄을 위/아래로 이동

lotto = random.sample(numbers, 6)
print(sorted(lotto))
