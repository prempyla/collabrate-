import React, { useState } from "react";

function App() {
  const [text, setText] = useState("");

  const handleChange = (e) => {
    setText(e.target.value);
  };

  return (
    <div>
      <input 
        type="text" 
        placeholder="Type something..."
        value={text}
        onChange={handleChange}
      />
      
      <p>{text}</p>
    </div>
  );
}

export default App;

