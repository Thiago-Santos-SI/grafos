def max_visitas (g,v_g,s):
  value = {}
  for i in g.vertices:
    if v_g[i]['ID'] == str(s):
      value = v_g[i]

  count = 0
  for i in g.vertices:
    if v_g[i]['altura'] < value['altura']:
      count += 1

  return count
