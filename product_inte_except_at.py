numbers = [1, 2, 6, 5, 9]
response = [540, 270, 90, 108, 60]

numbers1 = [1, 7, 3, 4, 5]
response1 = [84, 12, 28, 21]

def get_products_of_all_ints_except_at_index(numbers):
    responses = []
    for number in range(len(numbers)):
        answer = 1
        if number == len(numbers) - 1:
            for x in numbers[:number]:
                answer = answer * x
        elif number == 0:
            for x in numbers[1:]:
                answer = answer * x
        else:
            for x in numbers[number+1:]:
                answer = answer * x
            for x in numbers[: number]:
                answer = answer * x
        responses.append(answer)

def get_products_of_all_ints_except_at_index2(numbers):
    responses = []
    multi_before = 1
    for number in range(len(numbers)):
        answer = 1
        for x in numbers[number+1:]:
            answer = answer * x
        answer = answer * multi_before
        multi_before = multi_before * numbers[number]
        responses.append(answer)
    response.append(multi_before)   
    print(responses)

def get_products_of_all_ints_except_at_index3(numbers):
    if len(numbers) < 3:
        raise IndexError("Need at least 3 numbers")
    before = [1] * len(numbers)
    last_multi = 1
    for x in range(len(numbers)):
        before[x] = last_multi 
        last_multi = last_multi * numbers[x]    
    last_index = len(numbers) -1
    before_multi = 1
    while last_index >= 0:
        before[last_index] = before[last_index] * before_multi
        before_multi = before_multi * numbers[last_index]
        last_index -=1
    print(before)


# get_products_of_all_ints_except_at_index2(numbers)
get_products_of_all_ints_except_at_index2(numbers1)
get_products_of_all_ints_except_at_index3(numbers1)

get_products_of_all_ints_except_at_index2(numbers)
get_products_of_all_ints_except_at_index3(numbers)