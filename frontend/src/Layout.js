import React from "react";
import Navbar from "./components/Navbar/Navbar";
import { Link, Outlet } from "react-router-dom";

function Layout() {
  return (
    <div>
      <Navbar />
      <div>
        <Outlet />
      </div>
    </div>
  );
}

export default Layout;
