# Course Schedule
# Problem Statement:
# You need to take n courses and these courses are labeled from 0 to n-1. 
# Few of these courses have prerequisites. You are given the prerequisites as a 
# list of pairs where each pair is of form : [x, y]  where to take course 'x', 
# you need to complete course 'y' before it. Given these pairs and also the 
# count of total courses n, you need to return the ordering in which the courses 
# should be taken. Note that there might be multiple possible answers, you need to just 
# return any one of them and if any answer does not exist, return an array having -1.

# first course depends on the second [1, 0] take zero before one

def build_graph(n, prerequisites):
    g = {}
    for c, d in prerequisites:
        l = g.get(d, [])
        l.append(c)
        g[d] = l
    for x in range(n):
        if x not in g:
            g[x] = []
    return g

def course_schedule(n, prerequisites):
    graph = build_graph(n, prerequisites)
    t = [0]
    seen = set()
    in_stack = set()
    cycle = [False]
    nodes = []
    def dfs(course, graph):
        t[0] += 1
        start_time = t[0]
        seen.add(course)
        in_stack.add(course)
        for c in graph[course]:
            if c in in_stack:
                cycle[0] = True
                return
            if c not in seen:
                seen.add(c)
                dfs(c, graph)
        t[0] += 1
        end_time = t[0]
        nodes.append((end_time, course))
        in_stack.remove(course)

    for n in graph:
        if n not in seen:
            dfs(n, graph)
            result = sorted(nodes, reverse=True)
            result = [n for t, n in result]
    if cycle[0]:
        return [-1]
    return result

def course_schedule_v2(n, prerequisites):
    graph = build_graph(n, prerequisites)
    seen = set()
    in_edges_cntr = {}
    for n in graph:
        in_edges_cntr[n] = 0

    def bsf(node, graph):
        q = []
        q.append(node)
        seen.add(node)
        while len(q) > 0:
            current = q.pop(0)
            for child in graph[current]:
                in_edges_cntr[child] = in_edges_cntr.get(child, 0) + 1
                if child not in seen:
                    q.append(child)
                    seen.add(child)
    for n in graph:
        if n not in seen:
            bsf(n, graph)
    schedule = []
    found = True
    print(graph)
    print(in_edges_cntr)
    while found:
        found_key = None
        for key in in_edges_cntr:
            if in_edges_cntr[key] == 0:
                found_key = key
                for r in graph[key]:
                    in_edges_cntr[r] = in_edges_cntr[r] - 1
                schedule.append(key)
                break
        if found_key is not None:
            in_edges_cntr.pop(found_key)
        else:
            found = False
    if len(schedule) == 0 or len(in_edges_cntr) > 0:
        return [-1]
    return schedule


# e = 4 
# prerequisites=[ [1, 0], [2, 0], [3, 1], [3, 2] ]

# e = 3
# p = [[0, 1], [1, 2],[2, 0]]

# print(course_schedule(e, p))
# # print(course_schedule(num, recs))
# course_schedule_v2(e, p)

# e = 3
# p = [[0, 1], [0, 2],[1, 2]]

# print(course_schedule(e, prerequisites))
# # print(course_schedule(num, recs))
# print(course_schedule_v2(e, prerequisites))

e = 3

p = [[0, 1], [1, 0]]
print(course_schedule(e, p))
# print(course_schedule(num, recs))
print(course_schedule_v2(e, p))
