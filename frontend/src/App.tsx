import React from 'react';
import './App.css';
import HomePage from './components/HomePage';
import SearchPage from './components/SearchPage';
import EditPage from './components/EditPage';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Box from './components/Box';

function App() {
  return (
    <Router>
    
        

        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/edit" element={<EditPage />} />
        </Routes>

        {/* Move this Box to the bottom */}
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: 'auto' }}>
          <Box width={500} height={100} backgroundColor="lightblue">
             <ul>
                <li>
                  <Link to="/">Home</Link>
                </li>
                <li>
                  <Link to="/search">Search Page</Link>
                </li>
                <li>
                  <Link to="/edit">Edit Page</Link>
                </li>
              </ul>
          </Box>
        </div>
    
    </Router>
  );
}

export default App;
