import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState<string>("Loading...");

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/data") // Fetch from Flask
      .then(response => setMessage(response.data.message))
      .catch(error => console.error("Axios Error:", error));
  }, []);

  return (
    <div>
      <h1>Flask + Tkinter + React</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
