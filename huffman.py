

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


def run(c):
    letters = int(input())
    arr = {}
    for _ in range(letters):
        A, B = input().split()
        """ print(A)
        print(B) """
        arr[A] = int(B)
    freq = (
        dict(sorted(arr.items(), key=lambda item: [item[1], item[0]], reverse=1)))
    a_view = freq.items()
    freq = list(a_view)
    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])

    print('caso', str(c+1)+':')
    # print(nodes[0][0])
    # print(huffmanCode)

    for k, v in huffmanCode.items():
        print(k, v)


if __name__ == '__main__':
    iter = int(input())
    for i in range(iter):
        run(i)
