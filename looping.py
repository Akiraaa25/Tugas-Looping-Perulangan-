# # # # # # # a = 0
# # # # # # # while a <= 100 :
# # # # # # #     print (a)
# # # # # # #     a+=5*3

# # # # # # # j = 1
# # # # # # # while(j<=10) :
# # # # # # #     k =1
# # # # # # #     while(k<=10):
# # # # # # #         print(j*k,end="")
# # # # # # #         k+=1
# # # # # # #         print()
# # # # # # #         j+=1

# # # # # # for i  in range (0,31,3) :
# # # # # #     print(i)

# # # # # for k in range (3):
# # # # #     print ("nurul fikri")

# # # # for m in range (1,6):
# # # #     for n in range (1,6):
# # # #         O = m*n
# # # #         print(O, end='')
# # # #         print()

# # # x = 1
# # # while x < 6:
# # #     print(x)
# # #     x += 1
# # # else:
# # #     print("jikalau")

numbers = [
 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]
q = 0
while q <= len(numbers):
    if numbers [q] % 2 :
        print (numbers[q])
    if numbers [q] == 553:
        break
    q+=1

x= 0  
for y in range(1, 20,2): 
    x += y
print( x)

for k in range (0,int(input())):
    for l in range (0,k+1):
        print("*",end= " ")
    print( )