from configurations.env_configs import *
from services.api_service import *
# def graph():
#   hash = dict()
#   with open(_datasets_path() + 'connections.csv', 'rb') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#       if int(row[0]) in hash.keys():
#         hash[int(row[0])]['connections'].append(int(row[1]))
#       else:
#         connections1 = []
#         connections1.append(int(row[1]))
#         hash[int(row[0])] = {
#           # 'email': row[2],
#           'connections': connections1
#         }

#       if int(row[1]) in hash.keys():
#         hash[int(row[1])]['connections'].append(int(row[0]))
#       else:
#         connections2 = []
#         connections2.append(int(row[0]))
#         hash[int(row[1])] = {
#           # 'email': "",
#           'connections': connections2
#         }
#   return hash


def _request_data(uri):
    print("Sending request to:", uri)
    request = Request(uri)
    request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
    data = json.loads(urlopen(request).read())
    return data


# def graph(uri):
#     hash = dict()
#     connections = _request_data(uri)
#     for connection in connections:
#         account_id = int(connection['account_id'])
#         requestor_id = int(connection['requestor_id'])

#         if account_id in hash.keys():
#             hash[account_id]['connections'].append(requestor_id)
#         else:
#             connections1 = []
#             connections1.append(requestor_id)
#             hash[account_id] = {'connections': connections1}

#         if requestor_id in hash.keys():
#             hash[requestor_id]['connections'].append(account_id)
#         else:
#             connections2 = []
#             connections2.append(account_id)
#             hash[requestor_id] = {'connections': connections2}

#     return hash


def _neighbours(graph, user_id):
    if user_id in graph.keys():
        return graph[user_id]['connections']
    else:
        return set()


# def bfs(graph, user_id):
#     count = 0
#     commons = {}
#     visited, queue = set(), []
#     visited.add(user_id)
#     friends = _neighbours(graph, user_id)
#     queue = _enqueue(queue, visited, friends, 0)

#     while queue:
#         current = queue.pop(0)

#         if current['id'] not in visited:
#             count += 1
#             visited.add(current['id'])
#             connections = _neighbours(graph, current['id'])
#             if connections is not None:
#                 queue = _enqueue(queue, visited, connections,
#                                  current['level'] + 1)

#                 if current['id'] not in friends:
#                     mutuals = _common_friends(graph, user_id, current['id'])
#                     commons[current['id']] = {
#                         # 'email': graph[current['id']]['email'],
#                         'parent': user_id,
#                         # 'commons': mutuals,
#                         'level': current['level'],
#                         'num_of_commons': len(mutuals)
#                     }
#     print count
#     return sorted(commons.items(), key=lambda x: (x[1]['num_of_commons'], -x[1]['level']), reverse=True)[0:20]


def _common_friends(graph, user1, user2):
    a = _neighbours(graph, user1)
    b = _neighbours(graph, user2)

    return set(a).intersection(b)


def _enqueue(queue, visited, arr, level):
    for i in arr:
        if i not in visited:
            queue.append({'id': i, 'level': level})
    return queue



from services.account_service import *
from collections import OrderedDict

def _graph(uri):
    hash = dict()
    connections = _request_data(uri)
    for connection in connections:
        account_id = int(connection['account_id'])
        requestor_id = int(connection['requestor_id'])
        account_chapter = int(connection['account_chapter'])
        requestor_chapter = int(connection['requestor_chapter'])
        account_nationality = connection['account_nationality']
        requestor_nationality = connection['requestor_nationality']

        if account_id in hash.keys():
            hash[account_id]['connections'].append(requestor_id)
        else:
            connections1 = []
            connections1.append(requestor_id)
            # hash[account_id] = {'connections': connections1}
            # hash[account_id] = {'chapter': account_chapter}
            hash[account_id] = {
                'connections': connections1,
                'chapter': account_chapter,
                'nationality': account_nationality
            }

        if requestor_id in hash.keys():
            hash[requestor_id]['connections'].append(account_id)
        else:
            connections2 = []
            connections2.append(account_id)
            # hash[requestor_id] = {'connections': connections2}
            # hash[requestor_id] = {'chapter': requestor_chapter}
            hash[requestor_id] = {
                'connections': connections2,
                'chapter': requestor_chapter,
                'nationality': requestor_nationality
            }

    return hash


def _bfs(graph, user_id, user_data, params, decisions):
    commons = {}
    visited, queue = set(), []
    visited.add(user_id)
    friends = _neighbours(graph, user_id)
    queue = _enqueue(queue, visited, friends, 0)

    while queue:
        current = queue.pop(0)

        if current['level'] > 6:
            break 

        if params['chapter']:
            if graph[current['id']]['chapter'] != user_data['chapter']:
                continue

        if params['nationality']:
            if graph[current['id']]['nationality'] != user_data['nationality']:
                continue

        # continue if 1: accept or 2:reject
        if decisions.get(str(user_id)) is not None \
        and decisions[str(user_id)]['decisions'].get(str(current['id'])) is not None \
        and (decisions[str(user_id)]['decisions'][str(current['id'])] == 1
        or decisions[str(user_id)]['decisions'][str(current['id'])] == 2):
            continue

        if current['id'] not in visited:
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
    return OrderedDict(sorted(commons.items(), key=lambda x: (x[1]['num_of_commons'], -x[1]['level']), reverse=True)[0:20])

# from mongodb import update_mutual_friend_recommendations

def process_mutual_friends(uri, params):
    networks = _graph(uri)
    decisions = APIService().get_request(DECISIONS_FILTER, "trackable_type=Account", 1000, 'dict')

    for key, value in networks.iteritems():
        print("processing mutual friends for account: ", key)

        best_recommendations = _bfs(networks, key, value, params, decisions)
        # update_mutual_friend_recommendations(best_recommendations)
        print("finished mutual friends for account: ", key)



if __name__ == '__main__':
    uri = 'http://0.0.0.0:3000/api/v4/re/connections'
    params = {
        'location': True,
        'chapter': True,
        'nationality': True
    }
    process_mutual_friends(uri, params)



