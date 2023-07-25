// src/components/HomePage.tsx
import React from 'react';
import ArticleList from './ArticleList';
import Box from './Box';
import { Link } from 'react-router-dom'; // Use 'Link' instead of 'BrowserRouter as Link'
import Nav from './Nav';

const HomePage: React.FC = () => {
  return (
    <div className="App">
      <div style={{ textAlign: 'center', margin: '0px' }}>
        <nav>
          <Box width={100} height={100} backgroundColor="lightpink">
            <ul>
              {/* Use 'Link' instead of 'BrowserRouter' */}
            
                <Link to="/search">Search Page</Link>
              
            </ul>
          </Box>
        </nav>
      </div>

      <h1>Welcome to My Homepage</h1>
      <ArticleList />
      <div className="SearchBar">
        <input type="text" placeholder="Enter your search here" />
        <button>Search</button>
      </div>
    </div>
  );
};

export default HomePage;
