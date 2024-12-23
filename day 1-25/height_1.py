heights = [156, 178, 165, 171, 187, 199]
total =0
for h in heights:
    total += h

students = 0
for a in heights:
    students += 1

avg = total/students

print(f"Total height = {total}")

print(f"Average height = {avg}")