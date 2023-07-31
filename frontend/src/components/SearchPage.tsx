import axios from 'axios';
import React, { useState } from 'react';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Logo from "../assets/artifindlogo.png";
import './SearchPage.css';
import { Container, InputAdornment, TextField } from "@mui/material";
import SearchIcon from '@mui/icons-material/Search';

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

interface SearchResult {
  title: string;
  link: string;
  description: string;
  date: string;
  source: string;
  sentiment: number[];
  bias: string;
}

const SearchPage: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [daysBack, setDaysBack] = useState('');
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);

  const handleSearch = () => {
    axios
      .get(`http://localhost:8000/search/${searchQuery}/${daysBack}`)
      .then((response) => {
        // Handle the response here
        console.log(response.data);
        setSearchResults(response.data); // Store the response in state
      })
      .catch((error) => {
        // Handle errors here
        console.error(error);
      });
  };

  return (
    <div className="SearchPage">
      <div className="Logo" style={{ display: 'flex', justifyContent: 'center', margin: '50px' }}>
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

      <Container maxWidth="md" sx={{ mt: 5, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <form onSubmit={handleSearch}>
          <TextField
            id="search"
            type="search"
            label="Search Artifind"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            sx={{ width: 600 }}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <Button variant="contained" onClick={handleSearch} sx={{ backgroundColor: '#f15025',
                '&:hover': {
                  backgroundColor: 'black', 
                   },
                    }}>
                    <SearchIcon style={{ color: 'white' }}/>
                  </Button>
                </InputAdornment>
              ),
            }}
          />
        </form>
        <div className="DaysBack" style={{ marginTop: '20px', display: 'flex', justifyContent: 'center' }}>
        <label style={{ marginRight: '10px' }}> Days back to search:</label>
          <input
            type="number"
            value={daysBack}
            onChange={(e) => setDaysBack(e.target.value)}
          />
        </div>
      </Container>

      {searchResults.length > 0 && (
        <Grid container spacing={2} className="SearchResults" marginLeft={'200px'}>
          <Grid item xs={12}>
            <Typography variant="h4">Search Results</Typography>
          </Grid>
          {searchResults.map((result, index) => (
            <Grid item xs={8} key={index} style={{ paddingBottom: '15px', backgroundColor: index % 2 === 0 ? '#f0f0f0' : '#ffffff', }}>
              <Grid container spacing={2}>
                <Grid item xs={12}>
                  <Typography variant="body1">Title: <a href={result.link} target="_blank" rel="noopener noreferrer">{result.title}</a></Typography>
                  <Typography variant="body1">Description: <span dangerouslySetInnerHTML={{ __html: result.description }} /></Typography>
                  <Typography variant="body1">Date: {result.date}</Typography>
                  <Typography variant="body1">Source: {result.source}</Typography>
                  {/* Add a check for the 'sentiment' field */}
                  <Typography variant="body1">Sentiment: {result.sentiment ? result.sentiment.join(', ') : 'N/A'}</Typography>
                  <Typography variant="body1">Bias: {result.bias}</Typography>
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
