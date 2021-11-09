import React, { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");

  async function fetchMessage() {
    const response = await fetch(`http://127.0.0.1:5000/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    setMessage(data.message);
    console.log(data.message);
  }

  return (
    <div className="App">
      <button onClick={(e) => fetchMessage()}>click to show message</button>
      <h3>{message}</h3>
    </div>
  );
}

export default App;
