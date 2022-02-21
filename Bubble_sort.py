'''def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def bubblesort(ls):
    for i in range(0,len(ls)):
        for j in range(i,len(ls)):
            if ls[i]>ls[j]:
                ls[i],ls[j]=swap(ls[i],ls[j])

    return ls

if __name__=='__main__':
    ls=[7,1,5,10,2]
    sortedls=bubblesort(ls)
    print(sortedls)'''

def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)

