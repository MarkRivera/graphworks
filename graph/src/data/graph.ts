import Vertex from "./vertex";

class Graph {
  vertices: { [value: number | string]: Vertex };
  count: number;

  constructor() {
    this.vertices = {};
    this.count = 0;
  }

  addVertex(value: string | number): Vertex {
    this.count++;
    let newVert = new Vertex(value);
    this.vertices[value] = newVert;
    return newVert;
  }

  addEdge(
    keyOne: string | number,
    keyTwo: string | number,
    weight: number = 0
  ) {
    if (!(keyOne in this.vertices)) this.addVertex(keyOne); // if this value doesn't exist in my vertices obj then add it
    if (!(keyTwo in this.vertices)) this.addVertex(keyTwo); // if this value doesn't exist in my vertices obj then add it

    this.vertices[keyOne].addConnection(this.vertices[keyTwo], weight);
  }

  get getAllVertices(): string[] | number[] {
    return Object.keys(this.vertices);
  }

  contains(vertex: string | number): boolean {
    return vertex in this.vertices;
  }

  values(): Vertex[] {
    return Object.values(this.vertices);
  }
}

let g = new Graph();

for (let i = 0; i < 8; i++) {
  g.addVertex(i);
}

g.addEdge(0, 1, 3);
g.addEdge(0, 7, 2);
g.addEdge(1, 3, 4);
g.addEdge(2, 2, 1);
g.addEdge(3, 6, 5);
g.addEdge(4, 0, 2);
g.addEdge(5, 2, 3);
g.addEdge(5, 3, 1);
g.addEdge(6, 2, 3);
g.addEdge(7, 1, 4);

Object.values(g.vertices).forEach(vert => {
  console.log(vert.getConnections());
});

export default Graph;
