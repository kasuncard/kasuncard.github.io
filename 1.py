import cgi

form = cgi.FieldStorage()
num1 = float(form.getvalue('num1'))
num2 = float(form.getvalue('num2'))

sum_result = num1 + num2

# Выводим результат только в случае успеха
print("Content-Type: text/plain\n")
print(sum_result)
