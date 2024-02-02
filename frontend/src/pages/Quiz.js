import React, { useState, useEffect, useCallback } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { TextField, Box, Button, Alert, Typography } from "@mui/material";

const pronounMappings = {
    "él/ella/Ud.": ["él", "ella", "usted", "Maria", "John", "Daniel", "Amanda", "la mujer", "el niño", "el hombre", "el perro"],
    "ellos/ellas/Uds.": ["ellos", "ellas", "ustedes", "Sofia y Daniel", "Amelia y Gabby", "John y Carmen", "las mujeres", "los niños", "los hombres", "los perros"],
    "nosotros": ["Maria y yo", "nosotros", "Julia y yo", "Pedro y yo", "Michael y yo"]
  };

function Quiz() {
  const navigate = useNavigate();
  const location = useLocation();
  const quizData = location.state?.quizData;
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [displayedPronoun, setDisplayedPronoun] = useState("");
  const [userAnswer, setUserAnswer] = useState('');
  const [feedback, setFeedback] = useState(null);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);
  const [firstAttempt, setFirstAttempt] = useState(true);

  const getRandomPronoun = useCallback((pronoun) => {
    const options = pronounMappings[pronoun];
    return options ? options[Math.floor(Math.random() * options.length)] : pronoun;
  }, []);

  useEffect(() => {
    if (!quizData) {
      navigate('/practice', { state: { redirected: true } });
    } else if (quizData?.length > 0) { 
      setDisplayedPronoun(getRandomPronoun(quizData[0].question.pronoun));
    }
  }, [quizData, getRandomPronoun, navigate]);

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
          setDisplayedPronoun(getRandomPronoun(quizData[currentQuestionIndex + 1].question.pronoun));
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
    return;
  }

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
        <Typography variant="h3" sx={{ mb: 6, mt: 2 }}>Your Score:</Typography>
        <Typography variant="h2" sx={{ textAlign: 'center', mb: 3 }}>{percentageScore}%</Typography>
        <Typography variant="h4" sx={{ textAlign: 'center', mb: 8 }}>{score} out of {totalQuestions} correct</Typography>
        <Button variant="contained" color="primary" onClick={handleBackToPractice} sx={{ mb: 11 }}>
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
        <Typography variant="h4" sx={{ mb: 6, paddingTop: '30px' }}>Question {currentQuestionIndex + 1}/{quizData.length}</Typography>
        <Typography variant="h5" sx={{ mb: 2, textAlign: 'center' }}>{formatTenseName(currentQuestion.question.tense)}</Typography>
        <Typography variant="h4" sx={{ mb: 7, textAlign: 'center' }}>
          <span style={{ fontWeight: 'normal' }}>{displayedPronoun} </span>
          <span style={{ fontWeight: 'bold' }}>{currentQuestion.question.verb}</span>
        </Typography>

        <Box sx={{ display: 'flex', flexDirection: 'row', justifyContent: 'center', alignItems: 'center', gap: 2, mb: 2 }}>
          <TextField
            type="text"
            value={userAnswer}
            onChange={(e) => setUserAnswer(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="answer"
            autoFocus
            sx={{ 
                width: '240px',
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
