def max_69_num(num):
    six_index=0
    str_num=str(num)
    for index in range(len(str_num)):
        if str_num[index]=='6':
            six_index=index
            break
    return int(str_num[:six_index]+'9'+str_num[six_index+1:])
num=int(input())
print(max_69_num(num))