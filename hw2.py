## 1. List（可更動的有序列表）

### 題目
- 建立一個包含數字 `[5, 10, 15, 20]` 的列表 `numbers`。
- 在 `numbers` 的末尾添加 `25`。
- 將 `numbers` 的第二個元素修改為 `12`。

---

## 2. Tuple（不可更動的有序列表）

### 題目
- 建立一個元組 `letters = ('a', 'b', 'c')`。
- 嘗試修改 `letters[0]` 為 `'z'`，會發生什麼？
- 訪問 `letters` 的第三個元素。

---

## 3. 列表的索引與切片

### 題目
- 訪問並列印 `grades = [12, 60, 15, 70, 90]` 的第三個元素。
- 將 `grades` 的第一個元素修改為 `100`。
- 使用切片取得 `grades` 中第二到第四個元素。

---

## 4. 列表的刪除與更改

### 題目
- 刪除 `grades` 中的第二個元素。
- 將 `grades` 的最後兩個元素替換為 `75` 和 `85`。
- 清空 `grades` 列表。

---

## 5. 列表的長度

### 題目
- 建立一個包含 8 個元素的列表並計算長度。
- 添加 2 個新元素後計算長度。
- 刪除前三個元素後計算長度。

---

## 6. 巢狀列表

### 題目
- 建立 `matrix = [[1, 2, 3], [4, 5, 6]]`。
- 訪問 `matrix` 第二個子列表的第一個元素。
- 修改 `matrix` 第一個子列表的第三個元素為 `9`。


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
