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
       <div style={{ textAlign: 'center', margin: '20px' }}>
        <nav>
          
          <Box width={500} height={100} backgroundColor="lightpink">
            
              <ul>
              <Link to="/">Home</Link>
              </ul>
              <ul>
              <Link to="/search">Search Page</Link>
              </ul>
              <ul>
              <Link to="/edit">Edit Page</Link>
              </ul>
            
          </Box>
        </nav>
        </div>
     
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/edit" element={<EditPage />} />
      </Routes>
    </Router>
  );
}

export default App;
