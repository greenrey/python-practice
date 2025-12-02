# 유연근무제
# 🔗 https://school.programmers.co.kr/learn/courses/30/lessons/388351

def solution(schedules, timelogs, startday):
    limits = [] # 출근 제한 시각 리스트
    for s in schedules:
        if s % 100 < 50: # 분 단위가 50분 미만일 때
            limits.append(s+10)
        else: # 분 단위가 50분 이상일 경우, +10분을 하면 60분을 초과하므로, 시 단위에도 변화를 주어야 한다.
            minute = (s % 100 + 10) % 60 
            hour = s // 100 + 1
            limits.append(hour * 100 + minute)
    
    answer = 0
    for i, t in enumerate(timelogs): # 각 직원마다 계산
        late = 0
        for j, e in enumerate(t): # 날짜별 출근 시각 추출
            if ((j+startday) % 7) not in [6, 0]: # 주말이 아닌 경우
                if e > limits[i]: # 출근 제한 시각 초과 시
                    late += 1 # 지각으로 산정
        if late == 0: # 지각을 한 번도 하지 않았을 경우 상품 수여
            answer += 1
    return answer
