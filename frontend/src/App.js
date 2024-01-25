import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./Layout";
import Home from "./pages/Home";
import Practice from "./pages/Practice";
import Conjugate from "./pages/Conjugate";
import About from "./pages/About";
import Quiz from "./pages/Quiz";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="practice" element={<Practice />} />
          <Route path="conjugate" element={<Conjugate />} />
          <Route path="about" element={<About />} />
          <Route path="quiz" element={<Quiz />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
