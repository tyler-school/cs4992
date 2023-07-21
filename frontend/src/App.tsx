import React from 'react';
import './App.css';
import HomePage from './components/HomePage';
import OtherPage from './components/OtherPage';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Box from './components/Box';

function App() {
  return (
    <Router>
       <div style={{ textAlign: 'center', margin: '20px' }}>
        <nav>
          
          <Box width={200} height={100} backgroundColor="lightpink">
            
              <ul>
              <Link to="/">Home</Link>
              </ul>
              <ul>
              <Link to="/other">Other Page</Link>
              </ul>
            
          </Box>
        </nav>
        </div>
     
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/other" element={<OtherPage />} />
      </Routes>
    </Router>
  );
}

export default App;
