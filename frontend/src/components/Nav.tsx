import React from 'react';
import './App.css';
import HomePage from './HomePage';
import SearchPage from './SearchPage';
import EditPage from './EditPage';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Box from './Box';

function Nav() {
  return (
    <Router>
       
     
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/edit" element={<EditPage />} />
      </Routes>
    </Router>
  );
}

export default Nav;
