def get_check_digit(id_num):
    check = ""
    for i, x in enumerate(id_num[-2::-1]):
        if i % 2 == 0:
            x = int(x)
            x *= 2
        check+=str(x)
    
    check_sum = 0
    for x in check:
        check_sum += int(x)
    
    return (10 - (check_sum % 10)) % 10
    
def check_valid(payload):
    if get_check_digit(payload) == int(payload[-1]):
        return True
    else:
        return False

    