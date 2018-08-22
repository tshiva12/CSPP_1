#define the simple_divide function here
def simple_divide(item, denom):
    # start a try-except block
    try:
        return item / denom
    except ZeroDivisionError:
        return 0


   
def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]
    

def main():
    data = input()
    l_data=data.split()
    l1=[]
    for element in l_data:
        l1.append(float(element))
    sample=input()
    index=int(sample)
    print(fancy_divide(l1,index))
    
if __name__ == "__main__":
    main()
