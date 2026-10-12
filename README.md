# Стартовий проєкт SIS-P01

1. Відкрийте проєкт у GitHub Codespaces (Code → Codespaces → Create codespace) або локально: `python3 -m venv .venv`, `source .venv/bin/activate`, `pip install -r requirements.txt`. Потрібен Python 3.12 або новіший; права адміністратора не потрібні.
2. Визначте свою задачу й набір даних за номером варіанта N: задача = `(N - 1) // 3 + 1`, набір = `(N - 1) % 3 + 1`. Правила задачі — у `student.md`, вхідні дані набору — у `data/NN_k.yaml` (NN — задача з двома цифрами, k — набір).
3. Реалізуйте функції у файлі `variants/variant_NN.py` (прибирайте `NotImplementedError`).
4. Запускайте відкриті тести: `pytest tests/test_variant_NN.py`. Вони містять лише приклади з опису; повний набір є у викладача.
5. Побудуйте артефакт на даних свого набору: `mkdir -p out && python run_task.py NN k > out/NN_k.yaml`.
6. Змінюйте лише свій файл у `variants/`, теку `out/` і `ANSWERS.md` (3-5 речень). Власні тести додавайте у `tests/test_my.py`.
