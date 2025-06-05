# 1. Declaración de variables
age = 25  # ejemplo
height = 1.75
complex_number = 3 + 4j

# 2. Área de un triángulo
base = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area_triangle = 0.5 * base * height_triangle
print(f"The area of the triangle is {area_triangle}")

# 3. Perímetro de un triángulo
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter_triangle = a + b + c
print(f"The perimeter of the triangle is {perimeter_triangle}")

# 4. Área y perímetro de un rectángulo
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f"Area of rectangle: {area_rectangle}")
print(f"Perimeter of rectangle: {perimeter_rectangle}")

# 5. Área y circunferencia de un círculo
radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Area of the circle: {area_circle}")
print(f"Circumference of the circle: {circumference}")

# 6. Ecuación y = 2x - 2
slope = 2
x_intercept = 1  # 0 = 2x - 2 -> x = 1
y_intercept = -2  # cuando x = 0
print(f"Slope: {slope}, x-intercept: {x_intercept}, y-intercept: {y_intercept}")

# 7. Slope y distancia entre dos puntos
x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Slope between points: {slope2}")
print(f"Euclidean distance: {distance}")

# 8. Comparación de pendientes
print(f"Slope from y=2x-2:")