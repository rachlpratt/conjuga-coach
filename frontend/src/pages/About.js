import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListItem from '@mui/material/ListItem';
import DoubleArrowIcon from '@mui/icons-material/DoubleArrow';

function About() {
  const imagePath = process.env.PUBLIC_URL + '/DALLE_img.png';

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 2, mt: 1 }}>

      <Box sx={{ display: 'flex', justifyContent: 'center', gap: 2, margin: 4, mt: 6 }}>
        
        <Box
          sx={{
            border: '10px solid white',
            boxShadow: 5, 
            borderRadius: '4px',
            width: '30%',
            height: '30%',
            display: 'flex', 
            justifyContent: 'center',
            transform: 'rotate(-8deg)',
            mt: 3
          }}
        >
          <img 
            src={imagePath} 
            alt="Home" 
            style={{ 
              display: 'block',
              maxWidth: '100%',
              height: 'auto',
              borderRadius: '4px'
            }} 
          />
        </Box>

        <Box sx={{ 
          boxShadow: 5, 
          padding: 3,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          minWidth: '300px',
          maxWidth: '500px'
        }}>
          <Typography variant="h3" component="div" sx={{ margin: 1 }}>
            About ConjugaCoach
          </Typography>
          <Typography variant="body1" maxWidth='90%' sx={{ mt: 3, mb: 3, textAlign: 'center' }}>
            For many, mastering verb conjugations can be one of the most challenging aspects of learning Spanish. 
            Given the many forms a verb can take based on mood, tense, person, and number, 
            it takes a lot of practice to feel comfortable conjugating verbs on the fly. 
          </Typography>
          <Typography variant="body1" maxWidth='90%' sx={{ mb: 3, textAlign: 'center' }}>
            This is why <span style={{ fontWeight: 'bold', color: '#6A0DAD' }}>ConjugaCoach</span> was created 
            – to allow Spanish learners to create customized conjugation practice quizzes that can be tailored 
            to their learning needs. Drilling these verb conjugations until they become second nature is one 
            of the most effective ways to elevate your Spanish grammar skills. 
          </Typography>
          <Typography variant="body1" maxWidth='90%' sx={{ mb: 3, textAlign: 'center', fontWeight: 'bold' }}>
            Let ConjugaCoach help you get one step closer to achieving your Spanish learning goals!
          </Typography>
        </Box>
      </Box>

      <Box sx={{ mt: 1, mb: 4 }}>
        <Typography variant="h4" gutterBottom>
          Coming Soon:
        </Typography>
        <Typography variant="h6" gutterBottom>
          Keep a lookout for these upcoming features currently in development:
        </Typography>
        <Box>
          {[
            "More verbs!",
            "Random quiz generation for quick practice",
            "Quiz animations",
            "Information section providing details about various moods and tenses",
            "Toggleable dark mode",
            "Mobile-friendly interface"
          ].map(feature => (
            <ListItem key={feature} disablePadding>
              <ListItemIcon sx={{ marginRight: '-7px' }}>
                  <DoubleArrowIcon color="primary"/>
                </ListItemIcon>
              <ListItemText primary={feature} />
            </ListItem>
          ))}
        </Box>
      </Box>
    </Box>
  );
}

export default About;
