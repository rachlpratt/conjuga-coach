import React from "react";
import { Box, Typography } from '@mui/material';

function Home() {
  const imagePath = process.env.PUBLIC_URL + '/home_img.jpg';

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        mt: 5,
        boxShadow: 5,
        maxWidth: '70%',
        paddingTop: '30px',
        mx: 'auto',
        paddingBottom: '30px',
      }}
    >
      <Box
        sx={{
          border: '10px solid white',
          boxShadow: 5, 
          borderRadius: '4px',
          width: '60%',
          display: 'flex', 
          justifyContent: 'center',
          mb: 4
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
          }} 
        />
      </Box>
      <Box
        sx={{
          textAlign: 'center'
        }}
      >
        <Typography variant="h1" component="h2" sx={{ fontSize: '2.25rem' }}>
          Welcome to ConjugaCoach!
        </Typography>
      </Box>
    </Box>
  );
}

export default Home;
