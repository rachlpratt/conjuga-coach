import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';

function Practice() {
  const navigate = useNavigate();
  const [verbs, setVerbs] = useState([]);
  const [tenses, setTenses] = useState([]);
  const [pronouns, setPronouns] = useState([]);
  const [numItems, setNumItems] = useState(10);
  const TENSE_OPTIONS = ["present", "preterite", "future"]
  const PRONOUN_OPTIONS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros", "ellos/ellas/Uds."]

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch("https://conjuga-coach-app.uk.r.appspot.com/api/generate_quiz", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          verbs, tenses, pronouns, num_items: numItems,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      navigate('/quiz', { state: { quizData: data } });
    } catch (error) {
      console.error("Fetching error: ", error);
    }
  };

  const handleCheckboxChange = (checked, value, setter) => {
    if (checked) {
      setter(prev => [...prev, value]);
    } else {
      setter(prev => prev.filter(item => item !== value));
    }
  };

  return (
    <div>
      <h2>Generate Quiz</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <h4>Select Verbs</h4>
          <input
            type="text"
            value={verbs.join(', ')}
            onChange={(e) => setVerbs(e.target.value.split(',').map(v => v.trim()))}
            placeholder="Enter verbs separated by commas"
          />
        </div>
        <div>
        <h4>Select Tenses</h4>
        {TENSE_OPTIONS.map(tense => (
          <label key={tense}>
            <input
              type="checkbox"
              value={tense}
              checked={tenses.includes(tense)}
              onChange={(e) => handleCheckboxChange(e.target.checked, tense, setTenses)}
            />
            {tense}
          </label>
        ))}
        </div>
        <div>
        <h4>Select Pronouns</h4>
        {PRONOUN_OPTIONS.map(pronoun => (
          <label key={pronoun}>
            <input
              type="checkbox"
              value={pronoun}
              checked={pronouns.includes(pronoun)}
              onChange={(e) => handleCheckboxChange(e.target.checked, pronoun, setPronouns)}
            />
            {pronoun}
          </label>
        ))}
        </div>
        <div>
          <h4>Select # of Questions</h4>
          <input
            type="number"
            value={numItems}
            onChange={(e) => setNumItems(parseInt(e.target.value))}
            placeholder="10"
          />
        </div>

        <button type="submit">Generate Quiz</button>
      </form>
    </div>
  );
}

export default Practice;
