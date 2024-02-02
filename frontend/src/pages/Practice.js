import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import {
  Alert,
  Autocomplete,
  Box,
  Button,
  Checkbox,
  Chip,
  CircularProgress,
  createFilterOptions,
  IconButton,
  Snackbar,
  TextField,
  Typography
} from "@mui/material";
import CheckBoxIcon from '@mui/icons-material/CheckBox';
import CheckBoxOutlineBlankIcon from '@mui/icons-material/CheckBoxOutlineBlank';
import CloseIcon from '@mui/icons-material/Close';

const checkedIcon = <CheckBoxIcon fontSize="small" />;
const filter = createFilterOptions();
const icon = <CheckBoxOutlineBlankIcon fontSize="small" />;

const TENSE_OPTIONS = ["present", "preterite", "imperfect", "conditional", "future",
"present_subjunctive", "imperfect_subjunctive_ra",
"imperfect_subjunctive_se", "present_progressive", 
"past_progressive", "present_perfect", "pluperfect", 
"future_perfect", "present_perfect_subjunctive", 
"pluperfect_subjunctive_ra", "pluperfect_subjunctive_se", 
"affirmative_imperative", "negative_imperative"]
const PRONOUN_OPTIONS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros", "ellos/ellas/Uds."]

function Practice() {
  const navigate = useNavigate();
  const location = useLocation();
  const [allVerbs, setAllVerbs] = useState([]);
  const [verbs, setVerbs] = useState([]);
  const [tenses, setTenses] = useState([]);
  const [pronouns, setPronouns] = useState([]);
  const [numItems, setNumItems] = useState(10);
  const [isLoading, setIsLoading] = useState(false);
  const [verbError, setVerbError] = useState("");
  const [tenseError, setTenseError] = useState("");
  const [pronounError, setPronounError] = useState("");
  const [numItemsError, setNumItemsError] = useState("");
  const [openSnackbar, setOpenSnackbar] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState("");

  const handleVerbsChange = (event, newValue) => {
    if (newValue.length <= 10) {
      setVerbs(newValue);
      if (newValue.length > 0) {
        setVerbError("");
      }
    }
  };

  const handleTensesChange = (event, newValue) => {
    if (newValue.includes('All Tenses')) {
      setTenses(tenses.length === TENSE_OPTIONS.length ? [] : TENSE_OPTIONS);
    } else {
      setTenses(newValue);
    }
    if (newValue.length > 0) {
      setTenseError("");
    }
  };

  const handlePronounsChange = (event, newValue) => {
    if (newValue.includes('All Pronouns')) {
      setPronouns(pronouns.length === PRONOUN_OPTIONS.length ? [] : PRONOUN_OPTIONS);
    } else {
      setPronouns(newValue);
    }
    if (newValue.length > 0) {
      setPronounError("");
    }
  };

  const handleNumItemsChange = (event) => {
    const value = event.target.value;
    if (!isNaN(value) && value.trim() !== '') {
      setNumItems(parseInt(value, 10));
      if (parseInt(value, 10) >= 1 && parseInt(value, 10) <= 50) {
        setNumItemsError("");
      }
    } else if (value.trim() === '') {
      setNumItems('');
      setNumItemsError("");
    }
  };

  const checkErrors = () => {
    let hasErrors = false;
  
    if (verbs.length === 0) {
      setVerbError("Please select at least one verb");
      hasErrors = true;
    } else {
      setVerbError("");
    }
  
    if (tenses.length === 0) {
      setTenseError("Please select at least one tense");
      hasErrors = true;
    } else {
      setTenseError("");
    }
  
    if (pronouns.length === 0) {
      setPronounError("Please select at least one pronoun");
      hasErrors = true;
    } else {
      setPronounError("");
    }
  
    if (isNaN(numItems) || numItems === '' || parseInt(numItems) < 1) {
      setNumItemsError("Must be at least 1");
      hasErrors = true;
    } else if (numItems > 50) {
      setNumItemsError("No more than 50");
      hasErrors = true;
    } else {
      setNumItemsError("");
    }
  
    return hasErrors;
  };

  const renderVerbsInput = (params) => {
    return (
      <TextField 
        {...params}
        placeholder="Select verbs (10 max)"
        error={!!verbError}
        helperText={verbError || ' '}
        FormHelperTextProps={{ style: { visibility: verbError ? 'visible' : 'hidden' } }}
        InputProps={{
          ...params.InputProps,
          startAdornment: verbs.map((verb, index) => (
            <Chip key={index} label={verb} size="small" />
          )),
        }}
      />
    );
  };

  const renderTensesInput = (params) => {
    const displayAllSelected = tenses.length === TENSE_OPTIONS.length;

    return (
      <TextField 
        {...params}
        placeholder="Select tenses"
        error={!!tenseError}
        helperText={tenseError || ' '}
        FormHelperTextProps={{ style: { visibility: tenseError ? 'visible' : 'hidden' } }}
        InputProps={{
          ...params.InputProps,
          startAdornment: (
            <>
              {displayAllSelected 
                ? <Chip label="ALL TENSES SELECTED" size="small" />
                : tenses.map((tense, index) => (
                    <Chip key={index} label={formatTenseName(tense)} size="small" />
                  ))
              }
            </>
          ),
        }}
      />
    );
  };

  const renderPronounsInput = (params) => {
    const displayAllSelected = pronouns.length === PRONOUN_OPTIONS.length;

    return (
      <TextField 
        {...params}
        placeholder="Select pronouns"
        error={!!pronounError}
        helperText={pronounError || ' '}
        FormHelperTextProps={{ style: { visibility: pronounError ? 'visible' : 'hidden' } }}
        InputProps={{
          ...params.InputProps,
          startAdornment: (
            <>
              {displayAllSelected 
                ? <Chip label="ALL PRONOUNS SELECTED" size="small" />
                : pronouns.map((pronoun, index) => (
                    <Chip key={index} label={pronoun} size="small" />
                  ))
              }
            </>
          ),
        }}
      />
    );
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

  const handleCloseSnackbar = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpenSnackbar(false);
  };

  const fetchWithTimeout = (url, options, timeout = 20000) => {
    return Promise.race([
      fetch(url, options),
      new Promise((_, reject) =>
        setTimeout(() => reject(new Error('Timeout')), timeout)
      ),
    ]);
  };

  useEffect(() => {
    if (location.state?.redirected) {
      setSnackbarMessage("No quiz data found. Please start the quiz from this page.")
      setOpenSnackbar(true);
    }
    const fetchVerbs = async () => {
      try {
        const response = await fetchWithTimeout("https://conjuga-coach-app.uk.r.appspot.com/api/verbs");
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        setAllVerbs(data);
      } catch (error) {
        console.error("Error fetching verbs: ", error);
        let errorMessage = 'Sorry, there was a problem fetching verbs.';
        if (error.message === 'Timeout') {
          errorMessage = 'Request timed out. Please try again.';
        } else if (!navigator.onLine) {
          errorMessage = 'No internet connection.';
        }
        setSnackbarMessage(errorMessage);
        setOpenSnackbar(true);
      }
    };

    fetchVerbs();
  }, [location]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    if (!checkErrors()) {
      try {
        const response = await fetchWithTimeout("https://conjuga-coach-app.uk.r.appspot.com/api/generate_quiz", {
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
        let errorMessage = 'Sorry, there was a problem fetching the quiz.';
        if (error.message === 'Timeout') {
          errorMessage = 'Request timed out. Please try again.';
        } else if (!navigator.onLine) {
          errorMessage = 'No internet connection.';
        }
        setSnackbarMessage(errorMessage);
        setOpenSnackbar(true);
      } finally {
          setIsLoading(false);
      }
    } else {
      setIsLoading(false);
    }
  };

  return (
    <Box sx={{ mt: 4 }} >
      <Box
        sx={{
          margin: 'auto',
          paddingX: 2,
          paddingTop: 3,
          paddingBottom: 5,
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
        <Typography variant="h4" sx={{ textAlign: 'center', paddingTop: '25px', paddingBottom: '35px' }}>Practice Quiz Options</Typography>
        {isLoading ? (
            <Box sx={{ 
              textAlign: 'center',
              justifyContent: 'center', 
              height: '300px',
              display: 'flex', 
              flexDirection: 'column', 
              alignItems: 'center',
              flexGrow: 1
            }}>
            <p>Loading quiz...</p>
            <CircularProgress />
          </Box>
        ) : (
          <form onSubmit={handleSubmit} style={{ width: '100%' }}>
          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 2 }}>
            <Box sx={{ maxWidth: '450px', width: '70%' }}>
                <Autocomplete
                  multiple
                  options={allVerbs}
                  getOptionLabel={(option) => option}
                  value={verbs}
                  size="small"
                  disableCloseOnSelect
                  onChange={handleVerbsChange}
                  filterOptions={(options, { inputValue }) => {
                    return options.filter(option => 
                      option.toLowerCase().startsWith(inputValue.toLowerCase())
                    );
                  }}
                  renderOption={(props, option, { selected }) => (
                    <li {...props}>
                      <Checkbox
                        icon={icon}
                        checkedIcon={checkedIcon}
                        checked={selected}
                        style={{ marginRight: 8 }}
                      />
                      {option}
                    </li>
                  )}
                  renderInput={renderVerbsInput}
                  sx={{ width: '100%' }}
                />
            </Box>
          </Box>

          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 2 }}>
            <Box sx={{ maxWidth: '450px', width: '70%' }}>
              <Autocomplete
                multiple
                size='small'
                options={['All Tenses', ...TENSE_OPTIONS]}
                value={tenses}
                filterOptions={(options, params) => {
                  const filtered = filter(options, params);
                  if (params.inputValue === '') {
                    return options;
                  }
                  return filtered;
                }}
                onChange={handleTensesChange}
                disableCloseOnSelect
                getOptionLabel={(option) => option === 'All Tenses' ? option : formatTenseName(option)}
                renderOption={(props, option, { selected }) => (
                  <li {...props}>
                    <Checkbox
                      icon={icon}
                      checkedIcon={checkedIcon}
                      checked={option === 'All Tenses' ? tenses.length === TENSE_OPTIONS.length : selected}
                      style={{ marginRight: 8 }}
                    />
                    {option === 'All Tenses' ? option : formatTenseName(option)}
                  </li>
                )}
                renderInput={renderTensesInput}
              />
            </Box>
          </Box>

          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 3 }}>
            <Box sx={{ maxWidth: '450px', width: '70%' }}>
            <Autocomplete
                multiple
                size='small'
                options={['All Pronouns', ...PRONOUN_OPTIONS]}
                value={pronouns}
                filterOptions={(options, params) => {
                  const filtered = filter(options, params);
                  if (params.inputValue === '') {
                    return options;
                  }
                  return filtered;
                }}
                onChange={handlePronounsChange}
                disableCloseOnSelect
                renderOption={(props, option, { selected }) => (
                  <li {...props}>
                    <Checkbox
                      icon={icon}
                      checkedIcon={checkedIcon}
                      checked={option === 'All Pronouns' ? pronouns.length === PRONOUN_OPTIONS.length : selected}
                      style={{ marginRight: 8 }}
                    />
                    {option}
                  </li>
                )}
                renderInput={renderPronounsInput}
              />
            </Box>
          </Box>

          <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 2, mb: 1 }}>
            <TextField
              type="number"
              label="# of Questions"
              value={numItems}
              onChange={handleNumItemsChange}
              variant="outlined"
              placeholder="10"
              error={!!numItemsError}
              helperText={numItemsError || ' '}
              FormHelperTextProps={{ style: { visibility: numItemsError ? 'visible' : 'hidden' } }}
              InputLabelProps={{
                shrink: true,
              }}
              sx={{ 
                width: '140px',
                '& .MuiInputBase-input': {
                  textAlign: 'center'
                },
                '& .MuiOutlinedInput-root': {
                  height: '40px'
                }
              }}
            />
            <Button type="submit" variant="contained" color="primary" size="small" sx={{ mt: '-25px' }}>
              Quiz me!
            </Button>
          </Box>
          </form>
        )}
      </Box>

      <Snackbar 
        open={openSnackbar}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert 
          severity="error" 
          sx={{ width: '100%', textAlign: 'center' }}
          action={
            <IconButton
              size="small"
              aria-label="close"
              color="inherit"
              onClick={handleCloseSnackbar}
            >
              <CloseIcon fontSize="small" />
            </IconButton>
          }
        >
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </Box>
  );
}

export default Practice;
