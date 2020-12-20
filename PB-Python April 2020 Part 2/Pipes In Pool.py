volume_pool = float(input())
pipe1_debit = float(input())
pipe2_debit = float(input())
hours_worker_absence = float(input())

pipe1_fill = pipe1_debit * hours_worker_absence
pipe2_fill = pipe2_debit * hours_worker_absence
total_fill = pipe1_fill + pipe2_fill

if total_fill <= volume_pool:
    percentages_total_fill = total_fill * 100 / volume_pool
    pipe1_percentages = pipe1_fill * 100 / total_fill
    pipe2_percentages = pipe2_fill * 100 / total_fill
    print(f"The pool is {percentages_total_fill:.2f}% full. Pipe 1: {pipe1_percentages:.2f}%. Pipe 2: {pipe2_percentages:.2f}%.")
else:
    liters_overflow = total_fill - volume_pool
    print(f"For {hours_worker_absence} hours the pool overflows with {liters_overflow:.2f} liters.")
