import React, { useState, useEffect } from "react";
import { 
  Autocomplete,
  Box,
  Button, 
  CircularProgress,
  TextField, 
  Table, 
  TableBody, 
  TableCell, 
  TableContainer, 
  TableHead, 
  TableRow,
  Typography, 
  Paper 
} from '@mui/material';

function Conjugate() {
  const [verb, setVerb] = useState('');
  const [allVerbs, setAllVerbs] = useState([]);
  const [conjugations, setConjugations] = useState({});
  const hasConjugations = Object.keys(conjugations).length > 0;
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    try {
      const response = await fetch(`https://conjuga-coach-app.uk.r.appspot.com/api/conjugate/${verb}`);
      const data = await response.json();
      setConjugations(data);
    } catch (error) {
    console.error('Error fetching conjugations:', error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    const fetchVerbs = async () => {
      try {
        const response = await fetch("https://conjuga-coach-app.uk.r.appspot.com/api/verbs");
        const data = await response.json();
        setAllVerbs(data);
      } catch (error) {
        console.error("Error fetching verbs:", error);
        // Handle error (e.g., set error state, show message, etc.)
      }
    };
  
    fetchVerbs();
  }, []);

  const pronouns = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros", "ellos/ellas/Uds."];
  const tableConfigurations = [
    {
      title: "Indicative",
      tenses: ["present", "preterite", "imperfect", "conditional", "future"],
      labels: ["Present", "Preterite", "Imperfect", "Conditional", "Future"],
    },
    {
      title: "Imperative",
      tenses: ["affirmative_imperative", "negative_imperative"],
      labels: ["Affirmative", "Negative"],
    },
    {
      title: "Progressive",
      tenses: ["present_progressive", "past_progressive"],
      labels: ["Present", "Past"]
    },
    {
      title: "Subjunctive",
      tenses: ["present_subjunctive", "imperfect_subjunctive_ra", "imperfect_subjunctive_se"],
      labels: ["Present", "Imperfect (-ra)", "Imperfect (-se)"]
    },
    {
      title: "Perfect",
      tenses: ["present_perfect", "pluperfect", "future_perfect"],
      labels: ["Present", "Pluperfect", "Future"]
    },
    {
      title: "Perfect Subjunctive",
      tenses: ["present_perfect_subjunctive", "pluperfect_subjunctive_ra", "pluperfect_subjunctive_se"],
      labels: ["Present", "Pluperfect (-ra)", "Pluperfect (-se)"]
    }
  ];

  const generateTableRows = (tenses) => {
    return pronouns.map((pronoun) => (
      <TableRow key={pronoun}>
        <TableCell sx={{ fontStyle: 'italic' }}>{pronoun}</TableCell>
        {tenses.map((tense) => (
          <TableCell key={tense}>{conjugations && (conjugations[tense]?.[pronoun] || '')}</TableCell>
        ))}
      </TableRow>
    ));
  };

  function generateTable(tenses, labels, title) {
    return (
      <TableContainer component={Paper} sx={{ boxShadow: 5, maxWidth: '70%', margin: 'auto', my: 4 }}>
        <Box sx={{ my: 2, mx: 2, textAlign: "center" }}>
          <Typography variant="h5">
            {title}
          </Typography>
        </Box>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell></TableCell>
              {labels.map((label, index) => (
                <TableCell key={index} sx={{ fontWeight: 'bold' }}>
                  {label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {generateTableRows(tenses)}
          </TableBody>
        </Table>
      </TableContainer>
    );
  }

  return (
    <div style={{ paddingBottom: '20px' }}>
      <Box sx={{ display: 'flex', flexDirection: 'row', justifyContent: 'center', alignItems: 'center', marginTop: 4, gap: 2 }}>
        <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
          <Autocomplete
            options={allVerbs}
            getOptionLabel={(option) => option}
            value={verb}
            onChange={(event, newValue) => {
              setVerb(newValue);
            }}
            filterOptions={(options, { inputValue }) => {
              return options.filter(option => 
                option.toLowerCase().startsWith(inputValue.toLowerCase())
              );
            }}
            renderInput={(params) => (
              <TextField 
                {...params} 
                label="Enter a Verb" 
                variant="outlined" 
              />
            )}
            size="medium"
            sx={{ width: 250 }}
          />
        <Button variant="contained" size="large" onClick={handleSubmit}>Conjugate</Button>
        </form>
      </Box>

      {isLoading ? (
        <CircularProgress style={{ display: 'block', margin: 'auto', marginTop: '200px' }} />
      ) : (
        hasConjugations && tableConfigurations.map((config, index) => (
          <div key={index}>
            {generateTable(config.tenses, config.labels, config.title)}
          </div>
        ))
      )}
    </div>
  );
}

export default Conjugate;
