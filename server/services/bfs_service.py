import csv, os

def graph():
  hash = dict()
  with open(_datasets_path() + 'connections.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      if int(row[0]) in hash.keys():
        hash[int(row[0])]['connections'].append(int(row[1]))
      else:
        connections1 = []
        connections1.append(int(row[1]))
        hash[int(row[0])] = {
          # 'email': row[2],
          'connections': connections1
        }

      if int(row[1]) in hash.keys():
        hash[int(row[1])]['connections'].append(int(row[0]))
      else:
        connections2 = []
        connections2.append(int(row[0]))
        hash[int(row[1])] = {
          # 'email': "",
          'connections': connections2
        }
  return hash


def _neighbours(graph, user_id):
  if user_id in graph.keys():
    return graph[user_id]['connections']
  else:
    return set()


def bfs(graph, user_id):
  count = 0
  commons = {}
  visited, queue = set(), []
  visited.add(user_id)
  friends = _neighbours(graph, user_id)
  queue = _enqueue(queue, visited, friends, 0)

  while queue:
    current = queue.pop(0)

    if current['id'] not in visited:
      count += 1
      visited.add(current['id'])
      connections = _neighbours(graph, current['id'])
      if connections is not None:
        queue = _enqueue(queue, visited, connections,
                        current['level'] + 1)

        if current['id'] not in friends:
          mutuals = _common_friends(graph, user_id, current['id'])
          commons[current['id']] = {
            # 'email': graph[current['id']]['email'],
            'parent': user_id,
            # 'commons': mutuals,
            'level': current['level'],
            'num_of_commons': len(mutuals)
          }
  print count
  return sorted(commons.items(), key=lambda x: (x[1]['num_of_commons'], -x[1]['level']), reverse=True)[0:20]


def _common_friends(graph, user1, user2):
  a = _neighbours(graph, user1)
  b = _neighbours(graph, user2)

  return set(a).intersection(b)


def _enqueue(queue, visited, arr, level):
  for i in arr:
    if i not in visited:
      queue.append({'id': i, 'level': level})
  return queue


def _datasets_path():
  return os.path.abspath("") + "/datasets/"




