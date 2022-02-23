def merge_sort(arr,key,desc):
    if len(arr)<=1:
        return
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left,key,desc)
    merge_sort(right,key,desc)
    merge_two_sorted_list(left,right,arr,key,desc)

def merge_two_sorted_list(a,b,arr,key,desc):
    i=j=k=0
    if desc==True:
        while i< len(a) and j<len(b):
            if a[i][key]>b[j][key]:
                arr[k]=a[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
            k+=1
    else:
        while i< len(a) and j<len(b):
            if a[i][key]<b[j][key]:
                arr[k]=a[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
            k+=1
    while i<len(a):
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1
        k+=1
        

if __name__ == '__main__':
    elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 4},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
    merge_sort(elements,key='time_hours',desc=True)
    print(elements)