# -*- coding: utf-8 -*-
"""InverseFactorial.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t9PwQSmzwbtWn3iaJ24W3gxtiWfJlCRk
"""

import math

class Integral:
  def __init__(self, p, a, b, n):
    self.p = p # Result of factorial
    self.a = a # Lower bound integral
    self.b = b # Upper bound integral
    self.n = n # Difference

  def Simpson(self):
    p, a, b, n = self.p, self.a, self.b, self.n
    fun = lambda p, x=0: math.e**(-x)*x**p
    res = fun(p, a)+fun(p, b)
    i = (b-a)/n
    for k in range(1,n):
      if k%2 == 0: res += 2*fun(p, a+k*i)
      else: res += 4*fun(p, a+k*i)
    return i*res/3

  def Trapezoid(self):
    p, a, b, n = self.p, self.a, self.b, self.n
    fun = lambda p, x=0: math.e**(-x)*x**p
    res = 0
    i = (b-a)/n
    for k in range(n):
      res += (fun(p, a+k*i)+fun(p, a+(k+1)*i))/2
    return i*res

  def Riemann(self):
    p, a, b, n = self.p, self.a, self.b, self.n
    fun = lambda p, x=0: math.e**(-x)*x**p
    res = 0
    i = (b-a)/n
    for k in range(n+1):
      res += fun(p, a+k*i)
    return i*res

class Approx:
  def __init__(self, f, y, k):
    self.f = f # Factorial function
    self.y = y # Number that want to seacrh it's inverse
    self.k = k # Number of iteration

  def Bisection(self):
    f, y, k = self.f, self.y, self.k
    a, b, p = 0, 0, 0
    while math.factorial(p) < y:
      p += 1
    a = p - 1
    b = p
    p = (a+b)/2
    for _ in range(k):
      if f(p) < y: a = (a+b)/2
      elif f(p) > y: b = (a+b)/2
      else: break
      p = (a+b)/2
    return p

def Automation():
  number = float(input("Input the number you want to search the factorial : "))
  upper = int(input("Input the number you want to the upper bound of the integral : "))
  dif = int(input("Input the number you want to how many iteration on the integral : "))
  iter = int(input("Input the number you want to how many iteration on the interpolation : "))
  integral = int(input("Select what integration method you want\n1. Simpson\n2. Trapezoid\n3. Riemann\n Input : "))
  interpolation = int(input("Select what interpolation method you want\n1. Bisection\nInput : "))
  if integral == 1: fun = lambda x: Integral(x, 0, upper, dif).Simpson()
  elif integral == 2: fun = lambda x: Integral(x, 0, upper, dif).Trapezoid()
  elif integral == 3: fun = lambda x: Integral(x, 0, upper, dif).Riemann()
  eq = Approx(fun, number, iter)
  if interpolation == 1: res = eq.Bisection()
  print(f"Inverse factorial of {number} is {res}")
  
Automation()