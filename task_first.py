def total_salary(file_path):
    total = 0
    count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            name, salary = line.split(',')
            salary = int(salary)
            total += salary
            count += 1
    
    average = total / count if count else 0
    return total, average

total, average = total_salary("/Users/julia/goit-pycore-hw-04/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
