import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import './SearchPage.css';

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
      <Typography variant="h3" className="SearchHeading" style={{ marginTop: '80px', marginBottom: '20px'}}>
        Search Page
      </Typography>
      <div className="SearchContainer">
        <div className="SearchBar">
          <TextField
            id="outlined-basic"
            label="Enter your search here"
            variant="outlined"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <Button variant="contained" onClick={handleSearch}>
            Search
          </Button>
        </div>
        <div className="DaysBack">
          <TextField
          id='outlined-basic'
          label='How many days back to look'
          variant='outlined'
          type='number'
          />
        </div>
      </div>
            
      {/* Display the search results */}
      {searchResults.length > 0 && (
        <div className="SearchResults">
          {searchResults.map((result, index) => (
            <div key={index} className="SearchResultItem">
              <Typography variant="body1">{result}</Typography>
            </div>
          ))}
        </div>
      )}
      
    </div>
    
  );
};

export default SearchPage;
