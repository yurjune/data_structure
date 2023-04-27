class Node {
  constructor(data, next) {
    this.data = data;
    this.next = next;
  }
}

class Queue {
  constructor() {
    this.front = null;
    this.tail = null;
    this.size = 0;
  }

  isEmpty() {
    return this.front == null;
  }

  enqueue(value) {
    this.size++;
    const node = new Node(value);
    if (this.isEmpty()) {
      this.front = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
  }

  dequeue() {
    if (this.isEmpty()) {
      return null;
    }
    this.size--;

    const result = this.front.data;

    if (this.front == this.tail) {
      this.front = null;
      this.tail = null;
    } else {
      this.front = this.front.next;
    }

    return result;
  }
}

let qq = new Queue();
qq.enqueue('A');
qq.enqueue('B');
qq.enqueue('C');
qq.enqueue('D');
qq.enqueue('E');

console.log(qq.isEmpty());
console.log(qq.dequeue());
console.log(qq.dequeue());
console.log(qq.dequeue());
console.log(qq.dequeue());
console.log(qq.dequeue());
console.log(qq.isEmpty());
