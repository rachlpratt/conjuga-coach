import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { TextField, Autocomplete, Checkbox, Button, Box, createFilterOptions} from "@mui/material";
import CheckBoxIcon from '@mui/icons-material/CheckBox';
import CheckBoxOutlineBlankIcon from '@mui/icons-material/CheckBoxOutlineBlank';
import Chip from '@mui/material/Chip';
import CircularProgress from '@mui/material/CircularProgress';

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
  const [allVerbs, setAllVerbs] = useState([]);
  const [verbs, setVerbs] = useState([]);
  const [tenses, setTenses] = useState([]);
  const [pronouns, setPronouns] = useState([]);
  const [numItems, setNumItems] = useState(10);
  const [isLoading, setIsLoading] = useState(false);


  const handleVerbsChange = (event, newValue) => {
    if (newValue.length <= 10) {
      setVerbs(newValue);
    }
  };

  const handleTensesChange = (event, newValue) => {
    if (newValue.includes('All Tenses')) {
      setTenses(tenses.length === TENSE_OPTIONS.length ? [] : TENSE_OPTIONS);
    } else {
      setTenses(newValue);
    }
  };

  const handlePronounsChange = (event, newValue) => {
    if (newValue.includes('All Pronouns')) {
      setPronouns(pronouns.length === PRONOUN_OPTIONS.length ? [] : PRONOUN_OPTIONS);
    } else {
      setPronouns(newValue);
    }
  };

  const handleNumItemsChange = (event) => {
    const value = event.target.value;
    if (!isNaN(value) && value.trim() !== '') {
      setNumItems(parseInt(value, 10));
    } else if (value.trim() === '') {
      setNumItems('');
    }
  };

  const renderVerbsInput = (params) => {
    return (
      <TextField 
        {...params}
        placeholder="Select verbs (10 max)"
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
    setIsLoading(true);
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
    } finally {
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
        <h2 style={{ textAlign: 'center', paddingTop: '30px' }}>Practice Quiz Options</h2>
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
          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 3 }}>
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

          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 3 }}>
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

          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 4 }}>
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

          <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 2, mb: 2 }}>
            <TextField
              type="number"
              label="# of Questions"
              value={numItems}
              onChange={handleNumItemsChange}
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
        )}
      </Box>
    </Box>
  );
}

export default Practice;
