import Nav from "./components/Nav";

// Context
import { AlgoContext } from "./hooks/useAlgos";

const algos = [
  {
    name: "Breadth First Search",
    file: null,
  },
  {
    name: "Djikstra's Algorithm",
    file: null,
  },
];

function App() {
  return (
    <AlgoContext.Provider value={algos}>
      <Nav />
    </AlgoContext.Provider>
  );
}

export default App;
