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
    const alertStyle = { maxWidth: '550px' }

    if (userAnswer.trim().toLowerCase() === correctAnswer.toLowerCase()) {
      setFeedback(<Alert severity="success" sx={alertStyle}>Correct!</Alert>);

      if (firstAttempt) {
        setScore(score + 1);
      }

      setTimeout(() => {
        if (currentQuestionIndex < quizData.length - 1) {
          setCurrentQuestionIndex(currentQuestionIndex + 1);
        } else {
          setShowScore(true);
        }
        setUserAnswer('');
        setFeedback(null);
        setFirstAttempt(true);
      }, 1000);
    } else {
      setFeedback(<Alert severity="error" sx={alertStyle}>Answer: <Typography variant="inherit" fontWeight="bold" display="inline">{correctAnswer}</Typography></Alert>);
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
            paddingX: 2,
            paddingTop: 3,
            paddingBottom: 1,
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
          <Box sx={{ textAlign: 'center', mb: 8 }}>
            <h1>{percentageScore}%</h1> 
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
          paddingX: 2,
          paddingTop: 3,
          paddingBottom: 5,
          height: '400px',
          maxWidth: '600px',
          backgroundColor: 'white',
          borderRadius: 1,
          boxShadow: 5,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}
      >
        <Box sx={{ mb: 2, paddingTop: '30px' }} >
          <h2>Question {currentQuestionIndex + 1}/{quizData.length}</h2>
        </Box>

        <Box sx={{ mb: 4, textAlign: 'center' }} >
          <h3>{formatTenseName(currentQuestion.question.tense)}</h3>
          <h2>
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
          <Button type="submit" variant="contained" color="primary" onClick={handleAnswerSubmit}>
            Check
          </Button>
        </Box>
        {feedback && (
          <Box sx={{ mt: 2 }}>
            {feedback}
          </Box>
        )}
      </Box>
    </Box>
  );
}

export default Quiz;
