def friendship_score(g, p):
    resultado = 0
    visitado = []
    triangulo = 0
    if g == None:
        return None

    if p == None:
        count = 0
        for vizinho in g.outedges_of(p):
            count += 1
        return count

        visitado.append(p)
        for vizinho in g.outedges_of(p):
            if (vizinho) == None:
                return g.outedges_of(p)
            resultado += 1
            # print(p)
            vertice_vizinho = g.opposite(vizinho, p)
            visitado.append(vertice_vizinho)
        count = 0
        copy_arr_triangulo = []
        if resultado >= 5:
            search_triangle = resultado * 2 + 1
            return search_triangle
        # print(visitado)
        for vizinho in g.outedges_of(p):
            # print(p)
            # print('aresta', vizinho)
            vertice_vizinho = g.opposite(vizinho, p)
            # print('vertice vizinho', vertice_vizinho)
            arr_triangulo = []
            arr_triangulo.append(vertice_vizinho)
            for vizinho_grau2 in g.outedges_of(vertice_vizinho):
                vertice_vizinho_grau2 = g.opposite(vizinho_grau2, vertice_vizinho)
                for i in visitado:
                    if vertice_vizinho_grau2 == i:
                        #   print('--------->', vertice_vizinho_grau2)
                        arr_triangulo.append(vertice_vizinho_grau2)

            # print(arr_triangulo)
            if len(copy_arr_triangulo) > 0:
                count1 = 0
                for i in copy_arr_triangulo:
                    for j in arr_triangulo:
                        if i == j:
                            count1 += 1
                count = count1
            # print('count', count)
            if len(arr_triangulo) == 3 and count != 3:
                triangulo += 1
                copy_arr_triangulo = arr_triangulo
                count = 0

                # resultado += 1
            # print('teresa', resultado)
            count = 0
            # print('triangulo', triangulo)
        a = triangulo + resultado
        # print(a)
        return a
