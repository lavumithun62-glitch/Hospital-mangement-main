import { useState } from "react";
import API from "../services/api";

export default function Appointments() {
  const [doctor_id, setD] = useState("");
  const [patient_id, setP] = useState("");

  const book = () => {
    API.post("/appointments", { doctor_id, patient_id })
      .then(() => alert("Booked"));
  };

  return (
    <div>
      <h2>Appointment</h2>
      <input onChange={e => setD(e.target.value)} placeholder="doctor id" />
      <input onChange={e => setP(e.target.value)} placeholder="patient id" />
      <button onClick={book}>Book</button>
    </div>
  );
}
