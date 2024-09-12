def solution(a, b):
    import datetime
    week_dict = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    day = datetime.date(2016, a, b)

    # 0:월요일, 1:화요일 ~
    # print(day.weekday())
    answer = week_dict[day.weekday()]

    return answer


a, b = 5, 24	#"TUE"

print(solution(a, b))