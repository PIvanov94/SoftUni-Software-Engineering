days_off = int(input())

minutes_need = 30000
minutes_play_days_off = days_off * 127
working_days = 365 - days_off
minutes_play_working_days = working_days * 63
total_minutes_play = minutes_play_working_days + minutes_play_days_off

if minutes_need >= total_minutes_play:
    minutes_left_year = minutes_need - total_minutes_play
    total_hours_left = minutes_left_year // 60
    total_minutes_left = minutes_left_year % 60
    print("Tom sleeps well")
    print(f"{total_hours_left} hours and {total_minutes_left} minutes less for play")
else:
    total_minutes_need = total_minutes_play - minutes_need
    total_hours_need = total_minutes_need // 60
    total_minutes_need_play = total_minutes_need % 60
    print("Tom will run away")
    print(f"{total_hours_need} hours and {total_minutes_need_play} minutes more for play")