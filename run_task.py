"""Запускає вашу реалізацію задачі на вхідних даних набору й друкує результат у форматі YAML.

Використання:  python run_task.py <задача 1..10> <набір 1..3>
Приклад:       python run_task.py 8 2 > out/08_2.yaml
Дані беруться з data/NN_k.yaml; реалізація — з variants/variant_NN.py.
"""
import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent


def load_variant(number):
    path = ROOT / "variants" / f"variant_{number:02d}.py"
    spec = importlib.util.spec_from_file_location(f"variant_{number:02d}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 1
    task, number = int(argv[1]), int(argv[2])
    data = yaml.safe_load((ROOT / "data" / f"{task:02d}_{number}.yaml").read_text(encoding="utf-8"))
    module = load_variant(task)
    for index, call in enumerate(data["calls"], start=1):
        print(f"# виклик {index}: {call['function']}")
        try:
            result = getattr(module, call["function"])(**call["args"])
        except ValueError as error:
            print(f"помилка: {error}")
            continue
        if isinstance(result, str):
            print(result)
        else:
            print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False, width=110), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
