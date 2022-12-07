import aocd

x = aocd.get_data(day=7, year=2022).split('\n')


def build_tree(input):
    root_node = {
        'path': '',
        'parent': None,
        'score': 0,
        'nodes': [],
        'files': []
    }
    current_node = root_node
    current_dir = []

    i = 0
    while i < len(input):
        item = input[i]
        if item[0] == '$':
            if item[2] == 'c':
                # cd
                new_dir = item[5:]
                if new_dir == '..':
                    current_dir.pop()
                    current_node = current_node['parent']
                elif new_dir == '/':
                    current_dir = ['']
                    current_node = root_node
                else:
                    current_dir.append(new_dir)
                    new_node = {
                        'path': '/'.join(current_dir),
                        'score': 0,
                        'parent': current_node,
                        'nodes': [],
                        'files': []
                    }
                    current_node['nodes'].append(new_node)
                    current_node = new_node
            else:
                # ls
                current_node['score'] = 0
        elif item[0] == 'd':
            # dir - we can ignore since they don't impact the scoring
            pass
        else:
            # file
            current_node['files'].append(item)
            size = int(item.split(' ')[0])
            current_node['score'] += size

        i += 1
    return root_node


tree = build_tree(x)


part_b = []

results = []
flatten_tree = []
def do_sum(node):
    if node is None:
        return 0
    partial_sum = node['score'] + sum(map(do_sum, node['nodes']))
    node['cumscore'] = partial_sum
    if partial_sum <= 100000:
        results.append(node)
    flatten_tree.append(node)

    if partial_sum >= needed_space:
        part_b.append(partial_sum)

    return partial_sum


used_space = do_sum(tree)

sum(map(lambda v: v['cumscore'], results))

unused_space = 70000000 - used_space
needed_space = max(30000000 - unused_space, 0)























