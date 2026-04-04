def check_income(income):
    if income >= 300000:
        return"目標達成！"
    elif income >= 100000:
        return"順調です"
    elif income >= 30000:
        return"副業軌道中"
    else:
        return"まだこれから"

print(check_income(300000))
print(check_income(50000))