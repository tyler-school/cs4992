import React, { useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid'; // Import the Grid component
import Logo from "../assets/artifind logo4.png";
import './SearchPage.css';

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

interface SearchResult {
  fact: string;
  length: number;
}

const SearchPage: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [daysBack, setDaysBack] = useState('');
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);

  const handleSearch = () => {
    axios
      .get('https://catfact.ninja/fact')
      .then((response) => {
        // Handle the response here
        console.log(response.data);
        // Extract the relevant data from the API response (this may vary depending on the API)
        const result: SearchResult = {
          fact: response.data.fact,
          length: response.data.length,
        };
        setSearchResults([result]); // Store the response in state
      })
      .catch((error) => {
        // Handle errors here
        console.error(error);
      });
  };

  return (
    <div className="SearchPage">
      <div className="Logo" style={{ display: 'flex', justifyContent: 'center',  margin: '50px' }}>
      <a href="http://localhost:3000">
  <Box 
    component="img"
    sx={{
      height: 100,
    }}
    alt="Artifind"
    src={Logo}
    />
    </a>
</div>
      <div className="SearchContainer">
        {/* Wrap the search bar in a Box component */}
        <Box
          component="form"
          sx={{
            '& > :not(style)': { m: 1, width: '25ch' },
          }}
          noValidate
          autoComplete="off"
        >
          <TextField
            id="outlined-basic"
            label="Search Artifind"
            variant="outlined"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
           <Button variant="contained" onClick={handleSearch}>
            Search
          </Button>
        </Box>
        <div className="DaysBack">
          <label>Days back to search: </label>
          <input
            type="number"
            value={daysBack}
            onChange={(e) => setDaysBack(e.target.value)}
          />
        </div>
      </div>
      {/* Display the search results */}
      {searchResults.length > 0 && (
        <Grid container spacing={2} className="SearchResults" marginLeft={'200px'}>
          <Grid item xs={12}>
            <Typography variant="h4">Search Results</Typography>
          </Grid>
          {searchResults.map((result, index) => (
            <Grid item xs={8} key={index} 
            style={{paddingBottom: '15px', backgroundColor: index % 2 === 0 ? '#f0f0f0' : '#ffffff', // Apply alternating row colors
}}>
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <Typography variant="body1">Fact:</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body1">{result.fact}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body1">Length:</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body1">{result.length}</Typography>
                </Grid>
              </Grid>
            </Grid>
          ))}
        </Grid>
      )}
    </div>
  );
};

export default SearchPage;