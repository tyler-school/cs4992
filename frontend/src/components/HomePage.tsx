// src/components/HomePage.tsx
import React, { useEffect, useState } from 'react';
import { Tooltip, Fab, Grid, Accordion, AccordionDetails, AccordionSummary, Box, Checkbox, FormControlLabel, FormGroup, Input, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TextField, Typography } from "@mui/material";
import { styled } from '@mui/material/styles';
import EditIcon from '@mui/icons-material/Edit';
import SearchIcon from '@mui/icons-material/Search';
import { WidgetsJSON } from '../types/widgets';
import DisplayWidgetComponent from './WidgetComponent';
import moveLastToFront from '../types/helpers';
import Logo from "../assets/artifindlogo.png";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

const API_URL = 'https://jsonplaceholder.typicode.com/todos/1'; // Example URL that provides JSON data
const LOCAL_API_URL = 'http://127.0.0.1:8000/home/temp';

const HomePage: React.FC = () => {

  var newWidgetsObj: WidgetsJSON = {
    widgets: [
      {
        searchTerm: "Northeastern University",
        numberOfDays: 30,
        articles: [
          {
            title: "NU-Title1",
            source: "NU-Source1",
            date: "NU-Date1",
            link: "NU-Link1",
            description: "blah blah blah"
          },
          {
            title: "NU-Title2",
            source: "NU-Source2",
            date: "NU-Date2",
            link: "NU-Link2",
            description: "blah blah blah"
          },
          {
            title: "NU-Title3",
            source: "NU-Source3",
            date: "NU-Date3",
            link: "NU-Link3",
            description: "blah blah blah"
          }
        ]
      },
      {
        searchTerm: "Katherine Docks",
        numberOfDays: 7,
        articles: [
          {
            title: "KD-Title1",
            source: "KD-Source1",
            date: "KD-Date1",
            link: "KD-Link1",
            description: "blah blah blah"
          },
          {
            title: "KD-Title2",
            source: "KD-Source2",
            date: "KD-Date2",
            link: "KD-Link2",
            description: "blah blah blah"
          },
          {
            title: "KD-Title3",
            source: "KD-Source3",
            date: "KD-Date3",
            link: "KD-Link3",
            description: "blah blah blah"
          }
        ]
      },
      {
        searchTerm: "England Cricket",
        numberOfDays: 90,
        articles: [
          {
            title: "EC-Title1",
            source: "EC-Source1",
            date: "EC-Date1",
            link: "EC-Link1",
            description: "blah blah blah"
          },
          {
            title: "EC-Title2",
            source: "EC-Source2",
            date: "EC-Date2",
            link: "EC-Link2",
            description: "blah blah blah"
          },
          {
            title: "EC-Title3",
            source: "EC-Source3",
            date: "EC-Date3",
            link: "EC-Link3",
            description: "blah blah blah"
          }
        ]
      }
    ]
  }

  const [data, setData] = useState(newWidgetsObj);

  useEffect(() => {
    const interval = setInterval(() => {
      // alert("Original JSON: " + newWidgetsObj.widgets[0].searchTerm)
      const modifiedWidgets = moveLastToFront(widgetsData!.widgets)
      const modifiedWidgetObj: WidgetsJSON = {
        widgets: modifiedWidgets
      }
      // alert("Data was set to: " + modifiedWidgets[0].searchTerm)
      setData(modifiedWidgetObj);
      // alert("Value of JSON: " + newWidgetsObj.widgets[0].searchTerm)
    }, 3000);

    return () => clearInterval(interval);

  }, [data]);


  // T1 - Uncomment T1 sections for the practice API call functionality
  // Practice JSON getting
  // const [testJsonString, setTestJsonString] = useState('');

  // TODO: I think I can just use set data from the other use effect I have, and that should set the data nicely

  // useEffect(() => {

  //   const fetchData = async () => {
  //     try {
  //       const response = await fetch(LOCAL_API_URL);

  //       if (!response.ok) {
  //         throw new Error('Network response was not ok');
  //       }

  //       const dataNameFour: WidgetsJSON = await response.json();

  //       if (!dataNameFour || !dataNameFour.widgets)


  //       const data = await response.json();
  //       setTestJsonString(data.widgets[0].searchTerm) // Assuming the JSON has that field
  //       console.log("TEST LOG HERE")
  //       console.log(data);
  //       console.log(newWidgetsObj);
  //     }
  //     catch (error) {
  //       console.error("Error fetching data: ", error);
  //     }
  //   };

  //   fetchData();

  //   // const fetchData = async () => {
  //   //   try {
  //   //     const response = await fetch(LOCAL_API_URL);
  //   //     const data = await response.json();
  //   //     setTestJsonString(data.widgets[0].searchTerm) // Assuming the JSON has that field
  //   //     console.log("TEST LOG HERE")
  //   //     console.log(data);
  //   //     console.log(newWidgetsObj);
  //   //   }
  //   //   catch (error) {
  //   //     console.error("Error fetching data: ", error);
  //   //   }
  //   // };

  //   // fetchData();
  // }, []);


  const [widgetsData, setWidgetsData] = useState<WidgetsJSON | null>(newWidgetsObj);

    useEffect(() => {
      async function fetchWidgetsData(): Promise<void> {

        try {
          const response = await fetch(LOCAL_API_URL);
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          const dataNameFive: WidgetsJSON = await response.json();
          setWidgetsData(dataNameFive);
        }
        catch (error) {
          console.error("Error fetching widgets data: ", error)
        }        
      }

      fetchWidgetsData();
    }, [])


    return (
      <div className="HomePage">
        <div className="Logo" style={{ display: 'flex', justifyContent: 'center', margin: '50px' }}>
            <Box
              component="img"
              sx={{
                height: 100,
              }}
              alt="Artifind"
              src={Logo}
            />
        </div>
  
      <Box sx={{
        width: "100%",
        paddingTop: "0px"
      }}>
  
        {/* T1 - Uncomment this */}
        {/* <h1>Stuff: {testJsonString}</h1>   */}
  
        <Tooltip title="Make a custom search now" arrow placement='bottom'>
          <Fab id="foo" variant="extended" href='/search' sx={{left: "35%", top: "2%", minWidth: "200px", width: "30%"}}>
            <SearchIcon sx={{mr: 1
            }} />
            Search now
          </Fab>
        </Tooltip>
  
        <Tooltip title="Edit the widgets on your home page" arrow placement='top-start' sx={{fontSize: "20px"}}>
            <Fab variant="extended" href='/edit' 
            sx={{position: "fixed", 
            bottom: "3%", 
            right: "3%", 
            backgroundColor: "#f15025",
            color: "white",
          '&:hover': {
            backgroundColor: "#191919",
          }
            }}>
              <EditIcon sx={{mr: 1}} />
              Edit
            </Fab>
        </Tooltip>
  
        <Box sx={{
          width: "75%",
          marginLeft: "12.5%",
          marginRight: "12.5%",
          marginTop: "5.5%"
        }}>
  
          {
            widgetsData?.widgets.map((widget) => {
              return <DisplayWidgetComponent searchTerm={widget.searchTerm} numberOfDays={widget.numberOfDays} articles={widget.articles} />
              // return <h1>{widget.searchTerm}</h1>
            })
          }
        </Box>
      </Box>
      </div>
    );
  };
  
export default HomePage;
