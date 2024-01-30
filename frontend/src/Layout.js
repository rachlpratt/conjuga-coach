import React from "react";
import { Outlet } from "react-router-dom";
import { ThemeProvider } from '@mui/material/styles';
import Navbar from "./components/Navbar/Navbar";
import theme from './theme/theme';

function Layout() {
  return (
    <ThemeProvider theme={theme}>
      <div>
        <Navbar />
        <div>
          <Outlet />
        </div>
      </div>
    </ThemeProvider>
  );
}

export default Layout;
