LEVEL = {'H': 3, 'M': 2, 'L': 1}

def build_utility_tree(scenarios, max_drivers=None):
    """
    Побудова дерева корисності, ранжування сценаріїв та відбір архітектурних драйверів.
    """
    seen_ids = set()
    for s in scenarios:
        sid = s['id']
        if sid in seen_ids:
            raise ValueError(f"Повторний ідентифікатор: {sid}")
        seen_ids.add(sid)
        
        imp = s.get('importance')
        diff = s.get('difficulty')
        if imp not in LEVEL:
            raise ValueError(f"Недопустима оцінка: {imp}")
        if diff not in LEVEL:
            raise ValueError(f"Недопустима оцінка: {diff}")

    # 1. Ранжування: за спаданням балу (importance * 10 + difficulty), за рівності — за id абеткою
    def score(s):
        return LEVEL[s['importance']] * 10 + LEVEL[s['difficulty']]

    ranked_scenarios = sorted(scenarios, key=lambda s: (-score(s), s['id']))
    ranking = [s['id'] for s in ranked_scenarios]

    # 2. Драйвери: важливість H і складність H або M, обмежені max_drivers
    drivers_list = [
        s['id'] for s in ranked_scenarios
        if s['importance'] == 'H' and s['difficulty'] in ('H', 'M')
    ]
    if max_drivers is not None:
        drivers_list = drivers_list[:max_drivers]

    # 3. Відкладені (deferred): важливість L і складність H
    deferred_list = [
        s['id'] for s in ranked_scenarios
        if s['importance'] == 'L' and s['difficulty'] == 'H'
    ]

    # 4. Дерево: атрибут -> уточнення -> [id у порядку ранжування]
    tree = {}
    for s in ranked_scenarios:
        attr = s['attribute']
        ref = s['refinement']
        if attr not in tree:
            tree[attr] = {}
        if ref not in tree[attr]:
            tree[attr][ref] = []
        tree[attr][ref].append(s['id'])

    # Сортування атрибутів та уточнень за назвою (зростанням)
    sorted_tree = {}
    for attr in sorted(tree.keys()):
        sorted_tree[attr] = {}
        for ref in sorted(tree[attr].keys()):
            sorted_tree[attr][ref] = tree[attr][ref]

    return {
        "tree": sorted_tree,
        "ranking": ranking,
        "drivers": drivers_list,
        "deferred": deferred_list
    }