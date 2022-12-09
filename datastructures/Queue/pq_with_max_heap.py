class MaxHeapPriorityQueue:
    def __init__(self, max_heap=True):
        self.items = []
        self.max_heap = max_heap

    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.percolate_up(len(self.items) - 1)

    def dequeue(self):
        if not self.items:
            return None

        item = self.items[0][0]
        self.items[0] = self.items[-1]
        self.items.pop()
        self.percolate_down(0)

        return item

    def peek(self):
        if not self.items:
            return None

        return self.items[0][0]

    def percolate_up(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        if self.max_heap:
            if self.items[index][1] > self.items[parent_index][1]:
                self.items[index], self.items[parent_index] = (
                    self.items[parent_index],
                    self.items[index],
                )
                self.percolate_up(parent_index)
        else:
            if self.items[index][1] < self.items[parent_index][1]:
                self.items[index], self.items[parent_index] = (
                    self.items[parent_index],
                    self.items[index],
                )
                self.percolate_up(parent_index)

    def percolate_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if left_child_index >= len(self.items):
            return

        if right_child_index >= len(self.items):
            if self.max_heap:
                if self.items[index][1] < self.items[left_child_index][1]:
                    self.items[index], self.items[left_child_index] = (
                        self.items[left_child_index],
                        self.items[index],
                    )
            else:
                if self.items[index][1] > self.items[left_child_index][1]:
                    self.items[index], self.items[left_child_index] = (
                        self.items[left_child_index],
                        self.items[index],
                    )
            return

        if self.max_heap:
            if (
                self.items[index][1] >= self.items[left_child_index][1]
                and self.items[index][1] >= self.items[right_child_index][1]
            ):
                return
            if self.items[left_child_index][1] > self.items[right_child_index][1]:
                self.items[index], self.items[left_child_index] = (
                    self.items[left_child_index],
                    self.items[index],
                )
                self.percolate_down(left_child_index)
