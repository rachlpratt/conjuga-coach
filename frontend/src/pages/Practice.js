import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { TextField, Autocomplete, Checkbox, FormControlLabel, Button, Box } from "@mui/material";

function Practice() {
  const navigate = useNavigate();
  const [allVerbs, setAllVerbs] = useState([]);
  const [verbs, setVerbs] = useState([]);
  const [tenses, setTenses] = useState([]);
  const [selectAllTenses, setSelectAllTenses] = useState(false);
  const [pronouns, setPronouns] = useState([]);
  const [selectAllPronouns, setSelectAllPronouns] = useState(false);
  const [numItems, setNumItems] = useState(10);
  const TENSE_OPTIONS = ["present", "preterite", "imperfect", "conditional", "future",
                         "present_subjunctive", "imperfect_subjunctive_ra",
                         "imperfect_subjunctive_se", "present_progressive", 
                         "past_progressive", "present_perfect", "pluperfect", 
                         "future_perfect", "present_perfect_subjunctive", 
                         "pluperfect_subjunctive_ra", "pluperfect_subjunctive_se", 
                         "affirmative_imperative", "negative_imperative"]
  const PRONOUN_OPTIONS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros", "ellos/ellas/Uds."]

  const handleSelectAllTenses = (event) => {
    setSelectAllTenses(event.target.checked);
    setTenses(event.target.checked ? TENSE_OPTIONS : []);
  };

  const handleSelectAllPronouns = (event) => {
    setSelectAllPronouns(event.target.checked);
    setPronouns(event.target.checked ? PRONOUN_OPTIONS : []);
  };

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

  useEffect(() => {
    setSelectAllTenses(tenses.length === TENSE_OPTIONS.length);
    setSelectAllPronouns(pronouns.length === PRONOUN_OPTIONS.length);
  }, [tenses, pronouns]);

  useEffect(() => {
    const fetchVerbs = async () => {
      try {
        const response = await fetch("https://conjuga-coach-app.uk.r.appspot.com/api/verbs");
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        setAllVerbs(data);
      } catch (error) {
        console.error("Error fetching verbs: ", error);
      }
    };

    fetchVerbs();
  }, []);

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
      navigate("/quiz", { state: { quizData: data } });
    } catch (error) {
      console.error("Fetching error: ", error);
    }
  };

  return (
    <Box sx={{ mt: 4 }} >
      <Box
        sx={{
          margin: 'auto',
          padding: 2,
          maxWidth: '600px',
          backgroundColor: 'white',
          borderRadius: 1,
          boxShadow: 5,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}
      >
        <h2 style={{ textAlign: 'center' }}>Practice Quiz Options</h2>
        <form onSubmit={handleSubmit} style={{ width: '100%' }}>
          <h4 style={{ textAlign: 'center' }}>Verbs</h4>
          <Box sx={{ textAlign: 'center', mb: 1 }}>
            <Autocomplete
              multiple
              options={allVerbs}
              getOptionLabel={(option) => option}
              value={verbs}
              onChange={(event, newValue) => {
                setVerbs(newValue);
              }}
              filterOptions={(options, { inputValue }) => {
                return options.filter(option => 
                  option.toLowerCase().startsWith(inputValue.toLowerCase())
                );
              }}
              renderInput={(params) => (
                <TextField {...params} variant="outlined" placeholder="Select verbs" />
              )}
            />
          </Box>

          <h4 style={{ textAlign: 'center' }}>Tenses</h4>
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 1 }}>
            <Box sx={{ textAlign: 'center', flex: 1, mr: 2 }}>
              <Autocomplete
                multiple
                options={TENSE_OPTIONS}
                getOptionLabel={(option) => formatTenseName(option)}
                value={tenses}
                onChange={(event, newValue) => {
                  setTenses(newValue);
                }}
                renderInput={(params) => (
                  <TextField {...params} variant="outlined" placeholder="Select tenses" />
                )}
              />
            </Box>
            <FormControlLabel
              control={
                <Checkbox
                  checked={selectAllTenses}
                  onChange={handleSelectAllTenses}
                />
              }
              label="All"
              sx={{ flexShrink: 0 }}
            />
          </Box>

          <h4 style={{ textAlign: 'center' }}>Pronouns</h4>
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 5 }}>
            <Box sx={{ textAlign: 'center', flex: 1, mr: 2 }}>
              <Autocomplete
                multiple
                options={PRONOUN_OPTIONS}
                getOptionLabel={(option) => option}
                value={pronouns}
                onChange={(event, newValue) => {
                  setPronouns(newValue);
                }}
                renderInput={(params) => (
                  <TextField {...params} variant="outlined" placeholder="Select pronouns" />
                )}
              />
            </Box>
            <FormControlLabel
              control={
                <Checkbox
                  checked={selectAllPronouns}
                  onChange={handleSelectAllPronouns}
                />
              }
              label="All"
              sx={{ flexShrink: 0 }}
            />
          </Box>

          <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 2, mb: 2 }}>
            <TextField
              type="number"
              label="# of Questions"
              value={numItems}
              onChange={(e) => setNumItems(parseInt(e.target.value))}
              variant="outlined"
              placeholder="10"
              sx={{ 
                width: '110px',
                '& .MuiInputBase-input': {
                  textAlign: 'center'
                },
                '& .MuiOutlinedInput-root': {
                  height: '40px'
                }
              }}
            />
            <Button type="submit" variant="contained" color="primary">
              Quiz me!
            </Button>
          </Box>
        </form>
      </Box>
    </Box>
  );
}

export default Practice;
