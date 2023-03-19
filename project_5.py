#반복문2

sample =[
    ['a','b','c'],
    ['A','B','C'],
    ['A-','B-','C-'],
]
print(sample[0][0])
for i in sample:
    print(i[0]+' ,'+i[1]+' ,'+i[2])

credits = ['a','b','c']
eng = credits[0]
math = credits[1]
kor = credits[2]
# 위에 세 줄과 
#eng, math, kor = ['a', 'b', 'c'] same
print(eng, math, kor)

for eng, math, kor in sample: 
    print(eng +','+ math +',' +kor) # why print all?


