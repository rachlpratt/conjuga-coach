import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

function Quiz() {
  const location = useLocation();
  const quizData = location.state.quizData;
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [userAnswer, setUserAnswer] = useState('');
  const [feedback, setFeedback] = useState(null);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);
  const [firstAttempt, setFirstAttempt] = useState(true);

  const handleAnswerSubmit = () => {
    const correctAnswer = quizData[currentQuestionIndex].answer;
    if (userAnswer.trim().toLowerCase() === correctAnswer.toLowerCase()) {
      setFeedback('Correct!');
      if (firstAttempt) {
        setScore(score + 1);
      }
  
      setTimeout(() => {
        if (currentQuestionIndex < quizData.length - 1) {
          setCurrentQuestionIndex(currentQuestionIndex + 1);
          setUserAnswer('');
          setFeedback(null);
          setFirstAttempt(true);
        } else {
          setShowScore(true);
        }
      }, 2000);
    } else {
      setFeedback(`Correct answer: ${correctAnswer}`);
      setFirstAttempt(false);
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      handleAnswerSubmit();
    }
  };

  if (!quizData) {
    return <p>Loading quiz...</p>;
  }

  if (showScore) {
    return (
      <div>
        <h2>Your Score</h2>
        <p>{score} out of {quizData.length}</p>
      </div>
    );
  }

  const currentQuestion = quizData[currentQuestionIndex];
  
  return (
    <div>
      <h2>Question {currentQuestionIndex + 1}/{quizData.length}</h2>
      <h3>{currentQuestion.question.tense}</h3>
      <p>{currentQuestion.question.pronoun} {currentQuestion.question.verb}</p>
      <input
        type="text"
        value={userAnswer}
        onChange={(e) => setUserAnswer(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="answer"
      />
      <button onClick={handleAnswerSubmit}>Submit Answer</button>
      {feedback && (
        <p style={{ color: feedback.startsWith('Correct!') ? 'green' : 'red' }}>
          {feedback}
      </p>
    )}
  </div>
  );
}

export default Quiz;
