// src/components/AboutPage.tsx
import React from 'react';
import './SearchPage.css';

const SearchPage: React.FC = () => {
  return (
    <div className="SearchPage">
      <h1>SearchWizard</h1>
      <div className="SearchContainer">
        <div className="SearchBar">
          <input type="text" placeholder="Enter your search here" />
          <button>Search</button>
        </div>
        <div className="DaysBack">
          <label>Days back to search:</label>
          <input type="number" />
        </div>
      </div>
    </div>
  );
};

export default SearchPage;

//Will want an edit page....
