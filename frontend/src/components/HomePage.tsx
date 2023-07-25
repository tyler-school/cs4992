import React, { useEffect, useState } from 'react';
import ArticleList from './ArticleList';
import Box from './Box';
import { Link } from 'react-router-dom';
import Nav from './Nav';

function fetchData() {
  const dataToSend = { name: "susan" }; // Create an object with the data to be sent

  return fetch("/api/hello/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataToSend),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}


const HomePage: React.FC = () => {
  const [apiData, setApiData] = useState(null);

  useEffect(() => {
    fetchData()
      .then((data) => {
        setApiData(data); // Save the API response data in the state
      });
  }, []);

  return (
    <div className="App">
      <div style={{ textAlign: 'center', margin: '0px' }}>
        <nav>
          <Box width={100} height={100} backgroundColor="lightpink">
            <ul>
              <li>
                <Link to="/search">Search Page</Link>
              </li>
            </ul>
          </Box>
        </nav>
      </div>

      <h1>Welcome to My Homepage</h1>
      {/* Render the API response data */}
      {apiData && <pre>{JSON.stringify(apiData, null, 2)}</pre>}
      <ArticleList />
      <div className="SearchBar">
        <input type="text" placeholder="Enter your search here" />
        <button>Search</button>
      </div>
    </div>
  );
};

export default HomePage;
