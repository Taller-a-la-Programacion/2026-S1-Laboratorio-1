#NO MODIFICAR ESTE ARCHIVO

import Laboratorio01;
import pytest;

    
def test_lab_1():
    assert Laboratorio01.calcularRenta(700000) == 0
    
def test_lab_2():
    assert Laboratorio01.calcularRenta(1000000) == 18300
    
def test_lab_3():
    assert Laboratorio01.calcularRenta(2000000) == 157000

def test_lab_4():
    assert isinstance(Laboratorio01.calcularRenta("2000000"), str) == isinstance("Error: El valor debe ser de tipo entero", str)

def test_lab_5():
    assert isinstance(Laboratorio01.calcularRenta(-2000000), str) == isinstance("Error: El valor debe ser mayor a CERO", str)

##################################################################
    
def test_lab_6():
    assert Laboratorio01.contadorDigitos(102039480, 0) == 3

def test_lab_7():
    assert Laboratorio01.contadorDigitos(132033483, 3) == 4

def test_lab_8():
    assert isinstance(Laboratorio01.contadorDigitos(132033483, 13), str) == isinstance("Error: El parámetro digito debe ser un valor menor a 10", str)

def test_lab_9():
    assert isinstance(Laboratorio01.contadorDigitos("132033483", 13), str) == isinstance("Error: El parámetro num debe ser de tipo entero", str)

def test_lab_10():
    assert isinstance(Laboratorio01.contadorDigitos(132033483, "13"), str) == isinstance("Error: El parámetro digito debe ser de tipo entero", str)

##################################################################

def test_lab_11():
    assert Laboratorio01.calculadora (1, 4, 8) == 12

def test_lab_12():
    assert Laboratorio01.calculadora (2, 4, 8) == -4
    
def test_lab_13():
    assert Laboratorio01.calculadora (3, 4, 8) == 32

def test_lab_14():
    assert Laboratorio01.calculadora (4, 4, 8) == 0.5

def test_lab_15():
    assert isinstance(Laboratorio01.calculadora (14, 4, 8), str) == isinstance("Error: El parámetro operacion debe ser un valor menor a 5", str)
