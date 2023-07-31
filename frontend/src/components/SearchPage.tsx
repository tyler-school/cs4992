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
import { RepeatOneSharp } from '@mui/icons-material';

interface SearchResult {
  url: string;
  length: number;

}

interface SearchInput {
  term: string;
  days: number;
}

const SearchPage: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [daysBack, setDaysBack] = useState('');
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);

  const handleSearch = () => {
    axios
      .get('http://127.0.0.1:8000/search/ukraine/2')
      .then((response) => {
        // Handle the response here
        console.log(response.data);
        // Extract the relevant data from the API response (this may vary depending on the API)
        if (response.data.length > 0) {
          const result: SearchResult = {
            url: response.data[0].url, // Assuming the URL is accessible as response.data[0].url
            length: response.data[0].url.length,
          };
          setSearchResults([result]); // Store the response in state
        }
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
          {/* Display top search result */}
          <Grid item xs={8} style={{ paddingBottom: '15px', backgroundColor: '#f0f0f0' }}>
            <Grid container spacing={2}>
              <Grid item xs={6}>
                <Typography variant="body1">Fact:</Typography>
              </Grid>
              <Grid item xs={6}>
                <Typography variant="body1">{searchResults[0].url}</Typography>
              </Grid>
              <Grid item xs={6}>
                <Typography variant="body1">Length:</Typography>
              </Grid>
              <Grid item xs={6}>
                <Typography variant="body1">{searchResults[0].length}</Typography>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      )}
    </div>
  );
};

export default SearchPage;