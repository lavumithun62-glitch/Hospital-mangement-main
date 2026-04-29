import { useState } from "react";
import API from "../services/api";

export default function Doctors() {
  const [name, setName] = useState("");

  const add = () => {
    API.post("/doctors", { name }).then(() => alert("Added"));
  };

  return (
    <div>
      <h2>Doctors</h2>
      <input onChange={e => setName(e.target.value)} />
      <button onClick={add}>Add</button>
    </div>
  );
}
