import math

# Show all names of module's math
print(dir(math))

# Trigonometric functions and their inverses:
# - sine (sin)  ->  arcsine (asin)
# - cosine (cos) ->  arccosine (acos)
# - tangent (tan) ->  arctangent (atan)
# - radians function convert "degrees" to "radians"
# - degrees function convert "radiants" to "degrees"

print("sine(pi):", math.sin(math.radians(180)))
print("tangent(pi/4):", math.tan(math.radians(45)))
print("cosine(pi/4):", math.cos(math.radians(45)))

print("arcsine(1):", math.asin(1), math.pi/2)

print(math.radians(90) == math.pi/2)

# Exponentation
print("Exponentation")

print("e:",math.e)
print("e^3:", math.exp(3))
print("ln(5):", math.log(5))
print("log{10}(10):", math.log10(10))
print("log{2}(8):", math.log2(8))
print("log{3}(9):", math.log(9, 3))
print("3^5:", math.pow(3, 5))


# general purpose

y = 4
print("ceil({}):".format(y), math.ceil(y))
print("floor({}):".format(y), math.floor(y))
print("trunc({}):".format(y), math.trunc(y))

x = 4.3
print("ceil({}):".format(x), math.ceil(x))
print("floor({}):".format(x), math.floor(x))
print("trunc({}):".format(x), math.trunc(x))

z = -4.3
print("ceil({}):".format(z), math.ceil(z))
print("floor({}):".format(z), math.floor(z))
print("trunc({}):".format(z), math.trunc(z))
