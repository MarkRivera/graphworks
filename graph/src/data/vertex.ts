class Vertex {
  value: string | number;
  connections: Map<Vertex, number>;

  constructor(value: string | number) {
    this.value = value;
    this.connections = new Map();
  }

  get details(): string {
    return `The current vertex is: ${this.value}, and is connected to these vertices: ${this.connections}.`;
  }

  addConnection(vertex: Vertex, weight: number = 0): void {
    this.connections.set(vertex, weight);
  }

  getConnections(): Map<Vertex, number> {
    return this.connections;
  }

  get getValue(): string | number {
    return this.value;
  }

  getWeight(vertex: Vertex): number | undefined {
    return this.connections.get(vertex);
  }
}

export default Vertex;
