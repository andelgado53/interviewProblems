
change = []
def minimum_change(amount):
    q = 0.25
    d = 0.10
    n = 0.05
    p = 0.01
    amount_to_change = amount
    if amount_to_change == 0:
        return 
    elif amount_to_change >= q:
        num_q = amount_to_change // q
        change.append(('q', int(num_q)))
        reminder = amount_to_change % q
        return minimum_change(round(reminder, 2))
    elif amount_to_change >= d:
        num_d = amount_to_change // d
        change.append(('d', int(num_d)))
        reminder = amount_to_change % d

        return minimum_change(round(reminder, 2))
    
    elif amount_to_change >= n:

        num_n = amount_to_change // n
        change.append(('n', int(num_n)))
        reminder = amount_to_change % n
        
        return minimum_change(round(reminder,2))
    
    elif amount_to_change >= p:
        num_p = amount_to_change / p
        change.append(('p', int(num_p)))
        return 

minimum_change(100000)
print(change)
