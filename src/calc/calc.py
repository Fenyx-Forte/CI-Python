"""calc.

Este módulo fornece implementações para as 4 operações básicas da matemática:
- Adição -> adicao(a, b)
- Subtração -> subtracao (a, b)
- Multiplicação -> multiplicacao (a, b)
- Divisão -> divisao (a, b)
"""


def adicao(a: float, b: float) -> float:
    """Retorna o valor a + b.

    Args:
        a (float): O primeiro número.
        b (float): O segundo número.

    Returns:
        float: O valor a + b.

    """
    return a + b


def subtracao(a: float, b: float) -> float:
    """Retorna o valor a - b.

    Args:
        a (float): O número minuendo.
        b (float): O número subtraendo.

    Returns:
        float: O valor a - b.

    """
    return a - b


def multiplicacao(a: float, b: float) -> float:
    """Retorna o valor a * b.

    Args:
        a (float): O primeiro número.
        b (float): O segundo número.

    Returns:
        float: O valor a * b.

    """
    return a * b


def divisao(a: float, b: float) -> float:
    """Retorna o valor a / b.

    Args:
        a (float): O dividendo.
        b (float): O divisor.

    Raises:
        ZeroDivisionError: Se "b" for zero.

    Returns:
        float: O resultado a / b.

    """
    try:
        return a / b
    except ZeroDivisionError as erro:
        mensagem_erro = "Divisao por zero!"
        raise ZeroDivisionError(mensagem_erro) from erro
