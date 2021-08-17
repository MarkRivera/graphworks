import { createContext, useContext } from "react";

let AlgoContext = createContext(null);
const useAlgos = () => useContext(AlgoContext);

export { AlgoContext, useAlgos };
