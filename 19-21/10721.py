def Step(s, step, max_step, need): #step - кто будет ходить need 1 - ЕКТ, 2 - Петя, 0 - Ваня 
    if s >= 30:
        print((step-1) % 3)
        return ((step-1) % 3 == need)
    
    if step > max_step:
        return False
    
    if (step % 3) == need:
        return(Step(s + 1, step + 1, max_step, need) or Step(s * 2, step + 1, max_step, need))
    else:
        return(Step(s + 1, step + 1, max_step, need) and Step(s * 2, step + 1, max_step, need))

print(Step(, 1, 3, 1))

Answ_19 = 0
# for s in range(1, 30):
#     if Step(s, 1, 3, 0):
#         Answ_19 = s

print(Answ_19)