a = input("number1 : ")   #輸入 type為string, 預設提示字numder1
b = input("number2 : ")
print(a + b)  #為string ex.a = 1, b = 2, 輸出 12

c = eval(input())  #eval(str) 將字串str當成有效表達式來求值並返回計算結果
d = eval(input())
print(c + d)       #為int ex.a = 1, b = 2, 輸出 3