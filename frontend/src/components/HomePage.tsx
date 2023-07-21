// src/components/HomePage.tsx
import React from 'react';
import ArticleList from './ArticleList';
const HomePage: React.FC = () => {
  return ( 
    <div className="App">
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