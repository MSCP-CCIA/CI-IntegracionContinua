from programa import es_primo
import pytest

# Casos de prueba
def test_numero_primo():
    assert es_primo(2) == True  # 2 es primo
    assert es_primo(3) == True  # 3 es primo
    assert es_primo(5) == True  # 5 es primo
    assert es_primo(7) == True  # 7 es primo
    assert es_primo(11) == True  # 11 es primo
    assert es_primo(13) == True  # 13 es primo
    assert es_primo(17) == True  # 17 es primo

def test_numero_no_primo():
    assert es_primo(1) == False  # 1 no es primo
    assert es_primo(4) == False  # 4 no es primo
    assert es_primo(6) == False  # 6 no es primo
    assert es_primo(9) == False  # 9 no es primo
    assert es_primo(15) == False  # 15 no es primo
    assert es_primo(20) == False  # 20 no es primo

def test_numero_negativo():
    assert es_primo(-7) == False  # Los números negativos no son primos
    assert es_primo(-11) == False  # Los números negativos no son primos

def test_numero_muy_grande():
    # Usando números grandes para comprobar la eficiencia
    assert es_primo(104729) == True  # 104729 es primo (número grande)
    assert es_primo(100003) == True  # 100003 es primo (número grande)
    assert es_primo(1000000) == False  # 1000000 no es primo