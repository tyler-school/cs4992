// WidgetComponent.tsx

import { Tooltip, Fab, Grid, Accordion, AccordionDetails, AccordionSummary, Box, Checkbox, FormControlLabel, FormGroup, Input, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TextField, Typography } from "@mui/material";
import React from "react";
import { Widget } from "../types/widgets";
import { styled } from '@mui/material/styles';


const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  }));

const DisplayWidgetComponent: React.FC<Widget> = ({ searchTerm, numberOfDays, articles }) => {

    var colorThing = "#a6bfe0"

    if(searchTerm == "Northeastern University") {
        colorThing = "#ebd798"
    }

    if(searchTerm == "England Cricket") {
        colorThing = "#ace3ca"
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
                <TableCell colSpan={1}>{searchTerm}</TableCell>
                </TableRow>

                {/* ROW 2 */}
                <TableRow>
                {/* Article 1 */}
                <Grid container spacing={2}>
                    <Grid item xs={12}>
                    <Item>{articles[0].title}</Item>                  
                    </Grid>
                    <Grid item xs={8}>
                    <Item>{articles[0].source}</Item>                  
                    </Grid>
                    <Grid item xs={4}>
                    <Item>{articles[0].date}</Item>                  
                    </Grid>
                </Grid>
                </TableRow>

                {/* ROW 3 */}
                <TableRow>

                <Box sx={{padding: "3%"}}>

                    {/* Article 2 */}
                    <Grid container spacing={2}>
                    <Grid item xs={12}>
                        <Item>{articles[1].title}</Item>                  
                    </Grid>
                    <Grid item xs={8}>
                        <Item>{articles[1].source}</Item>                  
                    </Grid>
                    <Grid item xs={4}>
                        <Item>{articles[1].date}</Item>                  
                    </Grid>
                    </Grid>

                </Box>

                </TableRow>

                {/* ROW 4 */}
                <TableRow>

                <Box sx={{padding: "3%"}}>

                    {/* Article 3 */}
                    <Grid container spacing={2}>
                    <Grid item xs={12}>
                        <Item>{articles[2].title}</Item>                  
                    </Grid>
                    <Grid item xs={8}>
                        <Item>{articles[2].source}</Item>                  
                    </Grid>
                    <Grid item xs={4}>
                        <Item>{articles[2].date}</Item>                  
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