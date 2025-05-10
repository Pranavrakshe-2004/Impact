list1 = list(map(int, input("Enter 4 integers for list1 (space-separated): ").split()))
list2 = list(map(int, input("Enter 4 integers for list2 (space-separated): ").split()))
index_pairs = [(0, 0), (1, 2), (3, 3)]
compatible = True
for i1, i2 in index_pairs:
    if list1[i1] <= list2[i2]:
        compatible = False
        break

if compatible:
    print("is a compatible array")
else:
    print("Not compatible array")=[1,2,3,4]
list2=[5,6,7,7]
if list1[0]>list2[0] and list1[1]>=list2[2] and list1[3]>=list2[3]:
    print(list1,"compatible array")
else:
    print("not compatible array")