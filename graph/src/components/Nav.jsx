import { useAlgos } from "../hooks/useAlgos";

function Nav() {
  const algos = useAlgos();

  return (
    <nav>
      <span>Algorithms</span>

      <div className="algoContainer">
        {algos.map(algo => (
          <div key={`${algo.name}`}>{algo.name}</div>
        ))}
      </div>
    </nav>
  );
}

export default Nav;
