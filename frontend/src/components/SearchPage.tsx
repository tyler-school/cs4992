import React, { useState } from 'react';
import axios from 'axios'; // If you choose to use Axios

const SearchPage: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [daysBack, setDaysBack] = useState('');
  const [searchResults, setSearchResults] = useState<string[]>([]);

  const handleSearch = () => {
    axios
      .get('https://catfact.ninja/fact')
      .then((response) => {
        // Handle the response here
        console.log(response.data);
        // Extract the relevant data from the API response (this may vary depending on the API)
        const result = response.data.fact;
        setSearchResults([result]); // Store the response in state
      })
      .catch((error) => {
        // Handle errors here
        console.error(error);
      });
  };

  return (
    <div className="SearchPage">
      <h1 className="SearchHeading">Search Page</h1>
      <div className="SearchContainer">
        <div className="SearchBar">
          <input
            type="text"
            placeholder="Enter your search here"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <button onClick={handleSearch}>Search</button>
        </div>
        <div className="DaysBack">
          <label>Days back to search:</label>
          <input
            type="number"
            value={daysBack}
            onChange={(e) => setDaysBack(e.target.value)}
          />
        </div>
      </div>
      {/* Display the search results */}
      {searchResults.length > 0 && (
        <div className="SearchResults">
          {searchResults.map((result, index) => (
            <div key={index} className="SearchResultItem">
              <p>{result}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default SearchPage;
