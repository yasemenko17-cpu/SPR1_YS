"""Відкриті тести задачі 5: складання сценарію якості.

Запуск: pytest tests/test_variant_05.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
import pytest
from conftest import load

SPEC = dict(attribute="продуктивність", source=" студент ", stimulus="відкриває  каталог", environment="300 користувачів",
            artifact="вебзастосунок", response="показує список", target={"metric": "p95", "value": 0.8, "unit": "с"})


def test_make_scenario():
    assert load(5).make_scenario(SPEC, ["Q-PERF-01"]) == {
        "id": "Q-PERF-02", "attribute": "продуктивність", "source": "студент", "stimulus": "відкриває каталог",
        "environment": "300 користувачів", "artifact": "вебзастосунок", "response": "показує список",
        "measure": "p95 ≤ 800 мс"}


def test_availability_measure():
    spec = {**SPEC, "attribute": "доступність", "target": {"value": 99.9, "unit": "%", "bound": "min"}}
    assert load(5).make_scenario(spec)["measure"] == "≥ 99,9 %"


def test_unknown_attribute():
    with pytest.raises(ValueError) as info:
        load(5).make_scenario({**SPEC, "attribute": "краса"})
    assert str(info.value) == "Невідомий атрибут: краса"


def test_render_markdown():
    module = load(5)
    text = module.render_markdown(module.make_scenario(SPEC))
    assert text == ("### Q-PERF-01. продуктивність\n- Джерело: студент\n- Стимул: відкриває каталог\n"
                    "- Середовище: 300 користувачів\n- Артефакт: вебзастосунок\n- Відповідь: показує список\n"
                    "- Міра: p95 ≤ 800 мс")
