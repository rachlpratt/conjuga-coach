import React from "react";
import { Box, Button, Typography, List, ListItem, ListItemText, ListItemIcon } from '@mui/material';
import DoubleArrowIcon from '@mui/icons-material/DoubleArrow';
import { Link } from 'react-router-dom';

function Home() {
  const imagePath = process.env.PUBLIC_URL + '/home_img.jpg';

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        mt: 2,
        maxWidth: '80%',
        paddingTop: '30px',
        mx: 'auto',
        paddingBottom: '30px',
      }}
    >

      <Box
        sx={{
          display: 'flex', 
          justifyContent: 'space-between',
          alignItems: 'center',
          width: '100%',
          mb: 4
        }}
      >
        <Typography variant="h1" component="h2" sx={{ fontSize: '2.25rem', textAlign: 'left', mr: 6, width: '750px' }}>
          Master Spanish verb conjugation with <span style={{ fontWeight: 'bold', color: '#6A0DAD' }}>ConjugaCoach</span>!
        </Typography>
        <Box
          sx={{
            border: '10px solid white',
            boxShadow: 5, 
            borderRadius: '4px',
            width: '65%',
            display: 'flex', 
            justifyContent: 'center',
            transform: 'rotate(5deg)',
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
              borderRadius: '4px',
              objectFit: 'contain'
            }} 
          />
        </Box>
      </Box>
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          width: '100%',
        }}
      >
        <Box sx={{ width: '45%', boxShadow: 5, marginRight: '10px', padding: '15px', paddingTop: '30px', mt: 4, paddingRight: '25px' }}>
          <Typography variant="h2" sx={{ fontSize: '1.75rem', fontWeight: 'bold', textAlign: 'center' }}>
          How does it work?
          </Typography>
          <List sx={{ mt: 2 }}>
            {[
              { title: "Select Your Verbs", description: " Choose from 200 commonly used Spanish verbs to tailor your practice. Our user-friendly search bar makes it easy to quickly select the verbs you’re looking for." },
              { title: "Customize Your Quiz", description: " Pick the pronouns and tenses you want to focus on. Trying to learn the subjunctive mood? Need to improve your formal commands? We’ve got you covered." },
              { title: "Set Your Pace", description: " Decide on the number of questions. Whether you want a brief review or an extensive practice, design the quiz that aligns with your study goals." },
              { title: "Learn and Improve", description: " Take your quiz. Get one wrong? That’s okay! ConjugaCoach gives immediate feedback with the correct answer so you can quickly master conjugations." }
            ].map((item, index) => (
              <ListItem key={index} sx={{ display: 'flex', flexDirection: 'row', textAlign: 'left' }}>
                <ListItemIcon sx={{ marginRight: '-7px' }}>
                  <DoubleArrowIcon color="primary"/>
                </ListItemIcon>
                <ListItemText 
                  primary={item.title} 
                  secondary={item.description}
                  primaryTypographyProps={{ sx: { fontWeight: 'bold' } }}
                  secondaryTypographyProps={{ sx: { fontSize: '0.92rem', color: 'gray' } }}
                />
              </ListItem>
            ))}
          </List>
        </Box>

        <Box sx={{ width: '45%', boxShadow: 5, padding: '20px', marginLeft: '50px' }}>
          <Typography variant="h5" sx={{ mt: 4, fontWeight: 'bold', textAlign: 'center', maxWidth: '360px', margin: 'auto', paddingTop: '10px' }}>
            Visit the <Link to="/practice" style={{ color: 'primary', fontWeight: 'bold' }}>Practice</Link> page or click the button below to get started!
          </Typography>
          <Box sx={{ mt: 4 }}>
            <Button 
              variant="contained" 
              color="primary" 
              component={Link} 
              to="/practice" 
              sx={{ 
                display: 'flex',
                margin: 'auto', 
                width: '150px', 
                height: '40px', 
                justifyContent: 'center', 
                alignItems: 'center'
                }}
            >
              Practice
            </Button>
          </Box>
          <Typography variant="h6" sx={{ mt: 4, fontWeight: 'bold', textAlign: 'center' }}>
            Explore Conjugations:
          </Typography>
          <Typography sx={{ mt: 1, fontSize: '1rem', textAlign: 'center', margin: 'auto', maxWidth: '360px', color: '#3B3B3B' }}>
            To see detailed verb conjugation tables including all moods and tenses, visit the <Link to="/conjugate" style={{ color: 'primary', fontWeight: 'bold' }}>Conjugate</Link> page and select a verb.
          </Typography>
          
          <Typography variant="h6" sx={{ mt: 4, fontWeight: 'bold', textAlign: 'center' }}>
            Learn More:
          </Typography>
          <Typography sx={{ mt: 1, fontSize: '1rem', textAlign: 'center', maxWidth: '360px', margin: 'auto', mb: 3, color: '#3B3B3B' }}>
            Visit our <Link to="/about" style={{ color: 'primary', fontWeight: 'bold' }}>About</Link> page to learn more about ConjugaCoach and to see what's coming in future updates.
          </Typography>
        </Box>
      </Box>
    </Box>
  );
}

export default Home;
