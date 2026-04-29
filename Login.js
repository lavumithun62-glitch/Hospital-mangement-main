import { useState } from "react";
import API from "../services/api";

export default function Login() {
  const [username, setUser] = useState("");
  const [password, setPass] = useState("");

  const login = () => {
    API.post("/login", { username, password })
      .then(res => alert(JSON.stringify(res.data)));
  };

  return (
    <div>
      <h2>Login</h2>
      <input onChange={e => setUser(e.target.value)} placeholder="username" />
      <input onChange={e => setPass(e.target.value)} placeholder="password" />
      <button onClick={login}>Login</button>
    </div>
  );
}
