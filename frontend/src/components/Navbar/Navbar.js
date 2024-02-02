import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, IconButton, Menu, MenuItem, useMediaQuery, Button, useTheme } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';

function Navbar() {
  const [anchorEl, setAnchorEl] = useState(null);
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const menuItems = [
    { label: 'Home', path: '/' },
    { label: 'Practice', path: '/practice' },
    { label: 'Conjugate', path: '/conjugate' },
    { label: 'About', path: '/about' },
  ];

  return (
    <AppBar position="static">
      <Toolbar sx={{ justifyContent: 'space-between' }}>
        <Link to="/" style={{ display: 'flex', alignItems: 'center', color: 'inherit', textDecoration: 'none' }}>
          <img 
            src="/app_logo.png" 
            alt="ConjugaCoach Logo" 
            style={{ 
              marginRight: '10px', 
              height: '40px',
              borderRadius: '5px',
              border: '1px solid white'
            }} />
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            ConjugaCoach
          </Typography>
        </Link>
        {isMobile ? (
          <>
            <IconButton
              edge="start"
              color="inherit"
              aria-label="menu"
              onClick={handleMenu}
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorEl}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              KeepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorEl)}
              onClose={handleClose}
            >
              {menuItems.map((item) => (
                <MenuItem key={item.label} onClick={handleClose} component={Link} to={item.path}>
                  {item.label}
                </MenuItem>
              ))}
            </Menu>
          </>
        ) : (
          <div>
            {menuItems.map((item) => (
              <Button 
                key={item.label} 
                color="inherit" 
                component={Link} 
                to={item.path}
                sx={{ marginX: 1 }}
              >
                {item.label}
              </Button>
            ))}
          </div>
        )}
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
