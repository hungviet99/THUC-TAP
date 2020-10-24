# Python ngày 7
```
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

1. Tìm độ dài của tập it_companies

2. Thêm 'Twitter' vào it_companies

3. Chèn nhiều công ty CNTT cùng một lúc vào bộ it_companies

4. Xóa một trong các công ty khỏi tập hợp it_companies

5. Sự khác biệt giữa remove và discard là gì

6. join A và B

7. Tìm A giao B

8. Liệt kê phần tử A là một tập hợp con của B

9. A và B có phải là tập hợp không

10. Nối A với B và B với A

11. Sự khác biệt đối xứng giữa A và B là gì

12. Xóa cacs set

13. Chuyển ages thành một sets và so sánh độ dài của list và sets, cái nào lớn hơn?

14. Giải thích sự khác biệt giữa các kiểu dữ liệu sau: string, list, tuple và set

15. _I am a teacher and I love to inspire and teach people._ Có bao nhiêu từ đã được sử dụng trong câu? Bạn chưa học các vòng lặp nhưng bạn có thể làm điều đó theo cách thủ công.

## Lý thuyết

### Tạo 1 set 

```
st = {'item1', 'item2', 'item3', 'item4'}
```

### Đếm set 

```
st = {'item1', 'item2', 'item3', 'item4'}
len(set)
```

### Kiểm tra sự tồn tại trong set 

```
st = {'item1', 'item2', 'item3', 'item4'}
print('item3' in st)
```

### Thêm các mục 

#### Thêm 1 mục
```
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```
#### Thêm nhiều mục

```
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

### Xóa các mục khỏi 1 tập hợp

```
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

- Xóa phần tử cuối cùng 

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
```

- Xóa hết các phần tử 

```
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

### Xóa set 

```
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

### Chuyển đổi list thành set

```
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)
```

### Join set

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

- Chèn 

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)
```

### Tìm các mục giao nhau 

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)
```
### Kiểm tra tập hợp con 

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

### Kiểm tra sự khác nhau giữa 2 set 

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) 
st1.difference(st2)
```

### Tìm sự khác nhau giữa 2 tập hợp 

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.symmetric_difference(st1)
```

### Join set 

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)
```
