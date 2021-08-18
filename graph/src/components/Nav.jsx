import { useAlgos } from "../hooks/useAlgos";
import "./Nav.css";

function Nav() {
  const algos = useAlgos();

  return (
    <nav>
      <span>Algorithms</span>

      <div className="algoContainer">
        {algos.map(algo => (
          <button key={`${algo.name}`} className="algo-btn">
            {algo.name}
          </button>
        ))}
      </div>
    </nav>
  );
}

export default Nav;
