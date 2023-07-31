// WidgetComponent.tsx

import { Button, Tooltip, Fab, Grid, Accordion, AccordionDetails, AccordionSummary, Box, Checkbox, FormControlLabel, FormGroup, Input, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TextField, Typography } from "@mui/material";
import React from "react";
import { Widget } from "../types/widgets";
import { styled } from '@mui/material/styles';
import theme from "../util/theme";
import OpenInNewIcon from '@mui/icons-material/OpenInNew';

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
}));

const TitleItem = styled(Paper)(({}) => ({
    backgroundColor: 'white',
    fontSize: '30px',
    fontWeight: 'bold',
    padding: '15px',
    textAlign: 'left',
    color: 'black'
}));

const ArticleTitle = styled(Paper)(({}) => ({
    backgroundColor: 'white',
    fontSize: '20px',
    padding: '15px',
    textAlign: 'left',
    color: 'black',
}));

const DateTitle = styled(Paper)(({}) => ({
    backgroundColor: 'white',
    fontSize: '20px',
    padding: '15px',
    textAlign: 'left',
    color: 'black',
}));

const DisplayWidgetComponent: React.FC<Widget> = ({ searchTerm, numberOfDays, articles }) => {

    var colorThing = "#e6e8e6"

    if(searchTerm == "Northeastern University") {
        colorThing = "#e6e8e6"
    }

    if(searchTerm == "England Cricket") {
        colorThing = "#e6e8e6"
    }

    return (

        <Box sx={{
            marginBottom: "5%"
          }}>
            <TableContainer component={Paper}>
            <Table sx={{ backgroundColor: colorThing}}>
            <TableBody>
                {/* ROW 1 */}
                <TableRow>
                    <Box sx={{padding: "3%", paddingBottom: "4%"}}>
                        <Grid container spacing={2}>
                            <Grid item xs={11}>
                                <TitleItem>{searchTerm}</TitleItem>                  
                            </Grid>
                        </Grid>
                    </Box>

                {/* <TableCell colSpan={1}>{searchTerm}</TableCell> */}
                </TableRow>

                {/* ROW 2 */}
                <TableRow>
                {/* Article 1 */}

                    <Box sx={{padding: "3%", paddingTop: "0%", paddingBottom: "4%",}}>

                        {/* Article 1 */}
                        <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <ArticleTitle>{articles[0].title}</ArticleTitle>                  
                        </Grid>
                        <Grid item xs={5}>
                            <DateTitle>{articles[0].date}</DateTitle>              
                        </Grid>
                        
                        <Grid item xs={7}>
                            <Button href={articles[0].link} target="_blank" sx={{fontSize: "20px", 
                            textTransform: "inherit", justifyContent: "flex-end", padding: '9.5px', paddingRight: '30px',
                            backgroundColor: "#f36a4c",
          color: "white",
        '&:hover': {
          backgroundColor: "#191919",
        }
          }} variant="contained" fullWidth endIcon={<OpenInNewIcon />}>{articles[0].source}</Button>
                        </Grid>

                        </Grid>

                    </Box>

                </TableRow>

                {/* ROW 3 */}
                <TableRow>

                    <Box sx={{padding: "3%", paddingTop: "0%", paddingBottom: "4%",}}>

                        {/* Article 2 */}
                        <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <ArticleTitle>{articles[1].title}</ArticleTitle>                  
                        </Grid>
                        <Grid item xs={5}>
                            <DateTitle>{articles[1].date}</DateTitle>              
                        </Grid>
                        
                        <Grid item xs={7}>
                            <Button href={articles[1].link} target="_blank" sx={{fontSize: "20px", 
                            textTransform: "inherit", justifyContent: "flex-end", padding: '9.5px', paddingRight: '30px', 
                            backgroundColor: "#f36a4c",
                            color: "white",
                          '&:hover': {
                            backgroundColor: "#191919",
                          }
                            }} variant="contained" fullWidth endIcon={<OpenInNewIcon />}>{articles[1].source}</Button>
                        </Grid>

                        </Grid>

                    </Box>

                </TableRow>

                {/* ROW 4 */}
                <TableRow>

                    <Box sx={{padding: "3%", paddingTop: "0%", paddingBottom: "4%",}}>

                        {/* Article 1 */}
                        <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <ArticleTitle>{articles[2].title}</ArticleTitle>                  
                        </Grid>
                        <Grid item xs={5}>
                            <DateTitle>{articles[2].date}</DateTitle>              
                        </Grid>
                        
                        <Grid item xs={7}>
                            <Button href={articles[2].link} target="_blank" sx={{fontSize: "20px", 
                            textTransform: "inherit", justifyContent: "flex-end", padding: '9.5px', paddingRight: '30px',
                            backgroundColor: "#f36a4c",
          color: "white",
        '&:hover': {
          backgroundColor: "#191919",
        }
          }}
           variant="contained" fullWidth endIcon={<OpenInNewIcon />}>{articles[2].source}</Button>
                        </Grid>

                        </Grid>

                    </Box>

                </TableRow>
            </TableBody>
            </Table>
        </TableContainer>
      </Box>
    )
};

export default DisplayWidgetComponent;