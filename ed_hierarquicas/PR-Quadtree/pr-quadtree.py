import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RegNode:
    def __init__(self, pos, data=0):
        self.pos = pos
        self.data = data

class PRQuadTreeNode:
    def __init__(self, topLeft, botRight):
        self.topLeft = topLeft
        self.botRight = botRight
        self.child = [None] * 4  # top-left, top-right, bottom-left, bottom-right
        self.isLeaf = True
        self.data = None

    def insert(self, node):
        if not self.in_boundary(node.pos):
            return False

        if self.isLeaf:
            if self.data is None:
                self.data = node
                return True
            else:
                self.subdivide()
                self.child[self.get_quadrant(self.data.pos)].insert(self.data)
                return self.child[self.get_quadrant(node.pos)].insert(node)
        else:
            return self.child[self.get_quadrant(node.pos)].insert(node)

    def search(self, pos):
        if not self.in_boundary(pos):
            return None
        if self.isLeaf:
            if self.data and self.data.pos.x == pos.x and self.data.pos.y == pos.y:
                return self.data
            return None
        return self.child[self.get_quadrant(pos)].search(pos)

    def in_boundary(self, pos):
        return (self.topLeft.x <= pos.x <= self.botRight.x and
                self.topLeft.y <= pos.y <= self.botRight.y)

    def subdivide(self):
        midX = (self.topLeft.x + self.botRight.x) // 2
        midY = (self.topLeft.y + self.botRight.y) // 2
        self.child[0] = PRQuadTreeNode(self.topLeft, Point2D(midX, midY))
        self.child[1] = PRQuadTreeNode(Point2D(midX+1, self.topLeft.y), Point2D(self.botRight.x, midY))
        self.child[2] = PRQuadTreeNode(Point2D(self.topLeft.x, midY+1), Point2D(midX, self.botRight.y))
        self.child[3] = PRQuadTreeNode(Point2D(midX+1, midY+1), self.botRight)
        self.isLeaf = False

    def get_quadrant(self, pos):
        midX = (self.topLeft.x + self.botRight.x) // 2
        midY = (self.topLeft.y + self.botRight.y) // 2
        if pos.x <= midX:
            return 2 if pos.y > midY else 0
        else:
            return 3 if pos.y > midY else 1

class PRQuadTree:
    def __init__(self, boundary):
        self.root = PRQuadTreeNode(Point2D(boundary[0], boundary[1]), Point2D(boundary[2], boundary[3]))

    def insert(self, x, y, data=0):
        self.root.insert(RegNode(Point2D(x, y), data))

    def search(self, x, y):
        result = self.root.search(Point2D(x, y))
        return result.data if result else None

    def window_query(self, topLeft, botRight):
        result = []
        self._window_query_helper(self.root, topLeft, botRight, result)
        return result

    def _window_query_helper(self, node, topLeft, botRight, result):
        if node is None or not node.in_boundary(topLeft) or not node.in_boundary(botRight):
            return
        if node.isLeaf:
            if node.data and topLeft.x <= node.data.pos.x <= botRight.x and topLeft.y <= node.data.pos.y <= botRight.y:
                result.append(node.data)
        else:
            for child in node.child:
                self._window_query_helper(child, topLeft, botRight, result)

    def nearest_neighbor(self, center, R):
        # This is a naive implementation that checks all points in the square area
        points_in_range = self.window_query(Point2D(center.x - R, center.y - R),
                                            Point2D(center.x + R, center.y + R))
        nearest = None
        min_dist = float('inf')
        for point in points_in_range:
            dist = math.sqrt((point.pos.x - center.x) ** 2 + (point.pos.y - center.y) ** 2)
            if dist < R and dist < min_dist:
                nearest = point
                min_dist = dist
        return nearest

# Exemplo de uso:
quadtree = PRQuadTree([0, 0, 100, 100])  # Define o limite da área
quadtree.insert(10, 10, 1)  # Insere um ponto no (10,10) com dado 1
quadtree.insert(20, 20, 2)  # Insere um ponto no (20,20) com dado 2
print(quadtree.search(10, 10))  # Busca pelo ponto (10,10)
print(quadtree.window_query(Point2D(0, 0), Point2D(30, 30)))  # Consulta janela
print(quadtree.nearest_neighbor(Point2D(15, 15), 10))  # Ponto mais próximo dentro de uma distância R
