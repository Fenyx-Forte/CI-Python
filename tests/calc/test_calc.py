"""test_calc.

Testes para o módulo "calc.py".
"""

import sys
from pathlib import Path

# Adiciona a pasta "src" ao sys.path
sys.path.append(str(Path("../src").resolve()))

import pytest

from src.calc import calc


def test_adicao() -> None:
    """Testes para a função adicao(a, b)."""
    assert calc.adicao(-1, -1) == -2
    assert calc.adicao(-1, 0) == -1
    assert calc.adicao(-1, 1) == 0
    assert calc.adicao(0, -1) == -1
    assert calc.adicao(0, 0) == 0
    assert calc.adicao(0, 1) == 1
    assert calc.adicao(1, -1) == 0
    assert calc.adicao(1, 0) == 1
    assert calc.adicao(1, 1) == 2


def test_subtracao() -> None:
    """Testes para a função subtracao(a, b)."""
    assert calc.subtracao(-1, -1) == 0
    assert calc.subtracao(-1, 0) == -1
    assert calc.subtracao(-1, 1) == -2
    assert calc.subtracao(0, -1) == 1
    assert calc.subtracao(0, 0) == 0
    assert calc.subtracao(0, 1) == -1
    assert calc.subtracao(1, -1) == 2
    assert calc.subtracao(1, 0) == 1
    assert calc.subtracao(1, 1) == 0


def test_multiplicacao() -> None:
    """Testes para a função multiplicacao(a, b)."""
    assert calc.multiplicacao(-1, -1) == 1
    assert calc.multiplicacao(-1, 0) == 0
    assert calc.multiplicacao(-1, 1) == -1
    assert calc.multiplicacao(0, -1) == 0
    assert calc.multiplicacao(0, 0) == 0
    assert calc.multiplicacao(0, 1) == 0
    assert calc.multiplicacao(1, -1) == -1
    assert calc.multiplicacao(1, 0) == 0
    assert calc.multiplicacao(1, 1) == 1


def test_divisao() -> None:
    """Testes para a função divisao(a, b)."""
    assert calc.divisao(-1, -1) == 1
    with pytest.raises(ZeroDivisionError):
        assert calc.divisao(-1, 0)
    assert calc.divisao(-1, 1) == -1
    assert calc.divisao(0, -1) == 0
    with pytest.raises(ZeroDivisionError):
        assert calc.divisao(0, 0)
    assert calc.divisao(0, 1) == 0
    assert calc.divisao(1, -1) == -1
    with pytest.raises(ZeroDivisionError):
        assert calc.divisao(1, 0)
    assert calc.divisao(1, 1) == 1
