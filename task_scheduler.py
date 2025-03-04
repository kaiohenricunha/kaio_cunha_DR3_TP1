class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

class TaskScheduler:
    def __init__(self):
        self.heap = MinHeap()

    def add_task(self, priority, task):
        # A tarefa é inserida como uma tupla (prioridade, descrição).
        # Prioridades menores indicam maior urgência.
        self.heap.insert((priority, task))

    def get_next_task(self):
        # Extrai a tarefa de maior prioridade (menor valor)
        task = self.heap.pop()
        return task[1] if task else None

# Exemplo de uso:
scheduler = TaskScheduler()
scheduler.add_task(2, "Fazer backup dos dados")
scheduler.add_task(1, "Responder e-mails urgentes")
scheduler.add_task(3, "Atualizar sistema")

print(scheduler.get_next_task())  # Saída: "Responder e-mails urgentes"
print(scheduler.get_next_task())  # Saída: "Fazer backup dos dados"
print(scheduler.get_next_task())  # Saída: "Atualizar sistema"
