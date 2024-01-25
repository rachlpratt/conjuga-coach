import React, { useState, useEffect } from "react";

function Practice() {
  const [quizData, setQuizData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("https://conjuga-coach-app.uk.r.appspot.com/api/generate_quiz", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            verbs: ["ir", "hacer", "beber"],
            tenses: ["present", "preterite", "negative_imperative"],
            pronouns: ["yo", "tú", "nosotros"],
            num_items: 5,
          }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        setQuizData(data);
        console.log("DATA:");
        console.log(data);
      } catch (error) {
        console.error("Fetching error: ", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Quiz Questions</h2>
      {quizData ? (
        <ul>
          {quizData.map((item, index) => (
            <li key={index}>
              <p>Verb: {item.question.verb}</p>
              <p>Pronoun: {item.question.pronoun}</p>
              <p>Tense: {item.question.tense}</p>
              <p>Answer: {item.answer}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading quiz...</p>
      )}
    </div>
  );
}

export default Practice;
