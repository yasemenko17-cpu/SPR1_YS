"""Відкриті тести задачі 1: класифікація вимог.

Запуск: pytest tests/test_variant_01.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
import pytest
from conftest import load

CASES = [
    ("Користувач обирає лікаря зі списку", "functional", None, []),
    ("Відповідь надходить із затримкою не більше 2 секунд", "quality", "ефективність виконання", []),
    ("Паролі зберігаються у зашифрованому вигляді", "quality", "безпека", []),
    ("Система переживає відмову сервера і швидко відновлюється", "quality", "ефективність виконання", ["надійність"]),
    ("Дані обробляються відповідно до закону про персональні дані", "constraint", None, []),
    ("Оплата проходить за стандартом PCI DSS", "constraint", None, []),
]


@pytest.mark.parametrize("text,kind,characteristic,also", CASES, ids=[f"T01-{i}" for i in range(len(CASES))])
def test_classify(text, kind, characteristic, also):
    M = load(1)
    assert M.classify_requirements([{"id": "R1", "text": text}]) == [
        {"id": "R1", "kind": kind, "characteristic": characteristic, "also": also}]


def test_keeps_order_and_ids():
    M = load(1)
    result = M.classify_requirements([{"id": "B", "text": "Оплата"}, {"id": "A", "text": "Простій системи"}])
    assert [r["id"] for r in result] == ["B", "A"]
