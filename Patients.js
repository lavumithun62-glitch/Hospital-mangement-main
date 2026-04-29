import { useState } from "react";
import API from "../services/api";

export default function Patients() {
  const [name, setName] = useState("");

  const add = () => {
    API.post("/patients", { name }).then(() => alert("Added"));
  };

  return (
    <div>
      <h2>Patients</h2>
      <input onChange={e => setName(e.target.value)} />
      <button onClick={add}>Add</button>
    </div>
  );
}
