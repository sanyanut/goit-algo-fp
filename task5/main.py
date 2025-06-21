import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def find_node_by_id(start_node, target_id):
    if start_node is None:
        return None
    if start_node.id == target_id:
        return start_node

    left_result = find_node_by_id(start_node.left, target_id)
    if left_result:
        return left_result

    right_result = find_node_by_id(start_node.right, target_id)
    return right_result


def update_tree_display(root_node, current_graph=None, current_pos=None):
    if current_graph is None or current_pos is None:
        tree = nx.DiGraph()
        pos = {root_node.id: (0, 0)}
        tree = add_edges(tree, root_node, pos)
    else:
        tree = current_graph
        pos = current_pos

        for node_id, data in tree.nodes(data=True):
            actual_node = find_node_by_id(root_node, node_id)
            if actual_node:
                data["color"] = actual_node.color
                data["label"] = actual_node.val

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.clf()
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=3000, node_color=colors
    )
    plt.title("Tree visualization")
    plt.draw()
    plt.pause(0.7)

    return tree, pos


def interpolate_color(start_rgb, end_rgb, fraction):
    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * fraction)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * fraction)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * fraction)
    return f"#{r:02x}{g:02x}{b:02x}"


def generate_color(step, total_steps):
    start_rgb = (50, 100, 100)
    end_rgb = (200, 250, 150)

    if total_steps == 0:
        return "#FFFFFF"

    fraction = step / (total_steps - 1) if total_steps > 1 else 0.0
    return interpolate_color(start_rgb, end_rgb, fraction)


def reset_node_colors(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        node.color = "lightgray"
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def dfs_visualize(root):
    if not root:
        print("Tree is empty for DFS.")
        return

    print("\n--- Visualization of (DFS) ---")
    plt.ion()
    plt.subplots(figsize=(10, 7))

    reset_node_colors(root)

    all_nodes_count = 0
    temp_q = deque([root])
    while temp_q:
        node = temp_q.popleft()
        if node:
            all_nodes_count += 1
            if node.left:
                temp_q.append(node.left)
            if node.right:
                temp_q.append(node.right)

    g, p = update_tree_display(root)

    stack = [root]
    visited_ids = set()
    step_counter = 0

    while stack:
        current_node = stack.pop()

        if current_node.id not in visited_ids:
            visited_ids.add(current_node.id)

            current_node.color = generate_color(step_counter, all_nodes_count)
            step_counter += 1

            g, p = update_tree_display(root, g, p)

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

    plt.ioff()
    print("DFS complete. Close the window to continue.")
    plt.show()


def bfs_visualize(root):
    if not root:
        print("Tree is empty for BFS.")
        return

    print("\n--- Visualization of (BFS) ---")
    plt.ion()
    plt.subplots(figsize=(10, 7))

    reset_node_colors(root)

    all_nodes_count = 0
    temp_q = deque([root])
    while temp_q:
        node = temp_q.popleft()
        if node:
            all_nodes_count += 1
            if node.left:
                temp_q.append(node.left)
            if node.right:
                temp_q.append(node.right)

    g, p = update_tree_display(root)

    queue = deque([root])
    visited_ids = set()
    step_counter = 0

    while queue:
        current_node = queue.popleft()

        if current_node.id not in visited_ids:
            visited_ids.add(current_node.id)

            current_node.color = generate_color(step_counter, all_nodes_count)
            step_counter += 1

            g, p = update_tree_display(root, g, p)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    plt.ioff()
    print("BFS complete. Close the window to continue.")
    plt.show()


def build_heap_tree(heap_array, index=0):
    if index >= len(heap_array):
        return None

    node = Node(heap_array[index])
    node.left = build_heap_tree(heap_array, 2 * index + 1)
    node.right = build_heap_tree(heap_array, 2 * index + 2)
    return node


min_heap_array = [
    0,
    1,
    3,
    4,
    5,
    10,
]
heap_root = build_heap_tree(min_heap_array)

# DFS
if heap_root:
    dfs_visualize(heap_root)

# BFS
if heap_root:
    bfs_visualize(heap_root)
