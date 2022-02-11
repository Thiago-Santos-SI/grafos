def comandos_parada(p, i):
    comandos = []
    for v in p.vertices:
        if p.outdegree_of(v) == 0:
            comandos.append(v)

    result = []
    for v in comandos:
        result.append(v)
    return result
