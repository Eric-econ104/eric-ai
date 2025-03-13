#答 1: List
numbers = [5, 10, 15, 20]
numbers.append(25)
numbers[1] = 12

#答 2: Tuple
letters = ('a', 'b', 'c')
letters[0] = 'z'  
# TypeError，元組沒辦法變動
print(letters[2])  

#答 3: 列表的索引與切片
grades = [12, 60, 15, 70, 90]
print(grades[2])  
grades[0] = 100
print(grades[1:4])  

#答 4: 列表的刪除與更改
del grades[1]
grades[-2,-1] = [75, 85]
grades.clear() 

#答 5: 列表的長度
data = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(data))  
data.extend([9, 10])
print(len(data))  
del data[:3]
print(len(data))  

#答 6: 巢狀列表
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][0])  
matrix[0][2] = 9
