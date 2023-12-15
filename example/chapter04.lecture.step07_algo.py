
# 1 입력 자료 생성
import random
dataset = []
for i in range (10) :
    r = random.randint(1,100)
    dataset.append(r)
print(dataset)

# 2 변수 초기화
vmax = vmin = dataset[0]

# 3 최댓값 /최솟값 구하기
for i in dataset :       # for구문으로 하나씩 들어오면서
    if vmax < i :       # if문으로 구분됨 참일시
        vmax = i          # 밑 블록 실행. 값 교체
    if vmin > i :
        vmin = i

# 4결과 출력
print('max=', vmax, 'min=', vmin)

# 1 오름차순 정렬
dataset=[3,5,1,2,4]
n = len(dataset)
for i in range(0, n-1) :
    for j in range(i+1, n) :          #비교하려고 인덱스=1 한거임
        if dataset[i] > dataset[j] :   # 처음에 i에 0이 들어감 즉 3이 들어감.
                                       # j는 5가 들어가겟지... 조건이 안맞음 ?
            tmp = dataset [i]          # 뭔말? tmp에 3저장 . 그래서 3의 자리에 1이 들어감.
            dataset[i] = dataset[j]    # 자리바꾸는, 값교체과정인거임 이게
            dataset[j] = tmp     # 자리 바꾸기를 반복하면서 값 교체되고 위치 바뀌고

    print(dataset)    # 회전 내용 보여줌

print(dataset)       # 1,2,3,4,5 이렇게 나와야함 오름차순이니까
print()



# 2 내림차순 정렬
dataset = [ 3,5,1,2,4]
n = len(dataset)
for i in range (0, n-1) :      # 5-1 즉 4회전하게 됨.
    for j in range(i+1, n) :    #
        if dataset[i] < dataset[j] :   # 3과 5를 비교함내림차순이란뜻이겠죠..
            tmp = dataset[i]
            dataset [i] = dataset[j]
            dataset[j] = tmp
    print(dataset)    # 각 회전 정렬내용 보여주삼
print(dataset)      # 5,4,3,2,1 이렇게 나오든가


# 이진 검색 알고리즘
dataset = [ 5, 10, 81, 22, 35, 55, 75, 103]
value = int(input("검색할 값 입력: "))

low = 0   #start 위치
high = len (dataset) - 1  #end위치 !! 근데 len은 왜 세는 거지? n번째때문에?
loc = 0   # local이란 뜻인가?
state = False  #상태변수

while (low <= high) :
    mid = (low+ high) // 2   #이게 뭔말이니.... mid가 로우+하이 / 2라고? 아 미드평균값

    if dataset [mid] > value : #중앙값이 큰 경우
        high = mid - 1  # 뭔말인데 이게.. 위치?
    elif dataset[mid] < value :  # 중앙값이 작은 경우
        low = mid + 1   #뭐라고....
    else :    #찾은 경우
        loc = mid    # 나중에 활용하려고 loc에 저장
        state = True
        break  #반복 exit

    if state :                 #false였는데 true로 바꿔줌
        print('찾은 위치 : %d 번째'%(loc+1))      #색인값 처음은 0이라서 +1해줘야한다
    else :
        print('찾는 값은 없습니다')










