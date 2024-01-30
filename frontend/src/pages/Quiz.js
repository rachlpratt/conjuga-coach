import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import { TextField, Box, Button, Alert, Typography } from "@mui/material";
import { useNavigate } from 'react-router-dom';

function Quiz() {
  const navigate = useNavigate();
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
      setFeedback(<Alert severity="success">Correct!</Alert>);
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
      }, 1000);
    } else {
      setFeedback(<Alert severity="error">Answer: <Typography variant="inherit" fontWeight="bold">{correctAnswer}</Typography></Alert>);
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

  const formatTenseName = (tense) => {
    const replacements = {
      "imperfect_subjunctive_ra": "Imperfect Subjunctive (-ra)",
      "imperfect_subjunctive_se": "Imperfect Subjunctive (-se)",
      "pluperfect_subjunctive_ra": "Pluperfect Subjunctive (-ra)",
      "pluperfect_subjunctive_se": "Pluperfect Subjunctive (-se)",
    };

    return replacements[tense] || 
      tense.split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1)) 
        .join(' '); 
  };

  if (showScore) {
    const handleBackToPractice = () => {
      navigate('/practice');
    };

    const totalQuestions = quizData.length;
    const percentageScore = Math.round((score / totalQuestions) * 100);

    return (
      <Box sx={{ mt: 4 }} >
        <Box
          sx={{
            margin: 'auto',
            padding: 2,
            maxWidth: '600px',
            minHeight: '400px',
            backgroundColor: 'white',
            borderRadius: 1,
            boxShadow: 5,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center'
          }}
        >
          <Box sx={{ mb: 5 }} >
            <h2>Your Score</h2>
          </Box>
          <Box sx={{ textAlign: 'center', mb: 10 }}>
            <h2>{percentageScore}%</h2> 
            <h4>{score} out of {totalQuestions} correct</h4>
          </Box>
          <Button variant="contained" color="primary" onClick={handleBackToPractice}>
            Another Quiz
          </Button>
        </Box>
      </Box>
    );
  }

  const currentQuestion = quizData[currentQuestionIndex];
  
  return (
    <Box sx={{ mt: 4 }} >
      <Box
        sx={{
          margin: 'auto',
          padding: 2,
          maxWidth: '600px',
          minHeight: '400px',
          backgroundColor: 'white',
          borderRadius: 1,
          boxShadow: 5,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}
      >
        <Box sx={{ mb: 3 }} >
          <h2>Question {currentQuestionIndex + 1}/{quizData.length}</h2>
        </Box>

        <Box sx={{ mb: 5, textAlign: 'center' }} >
          <h3 style={{ marginBottom: '15px' }}>{formatTenseName(currentQuestion.question.tense)}</h3>
          <h2 style={{ marginTop: '10px' }}>
            <span style={{ fontWeight: 'normal' }}>{currentQuestion.question.pronoun} </span>
            <span style={{ fontWeight: 'bold' }}>{currentQuestion.question.verb}</span>
          </h2>
        </Box>

        <Box sx={{ display: 'flex', flexDirection: 'row', justifyContent: 'center', alignItems: 'center', gap: 2, mb: 2 }}>
          <TextField
            type="text"
            value={userAnswer}
            onChange={(e) => setUserAnswer(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="answer"
            autoFocus
            sx={{ 
                width: '200px',
                '& .MuiInputBase-input': {
                  textAlign: 'center'
                },
                '& .MuiOutlinedInput-root': {
                  height: '40px'
                }
              }}
          />
          <Button type="submit" variant="contained" color="primary">
            Check
          </Button>
        </Box>
        {feedback && (
          <Box sx={{ textAlign: 'center' }}>
            <div style={{ color: feedback.props.severity === 'success' ? 'green' : 'red' }}>
              {feedback}
            </div>
          </Box>
        )}
      </Box>
    </Box>
  );
}

export default Quiz;
