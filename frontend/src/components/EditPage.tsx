import React, { useState } from 'react';
import { Grid, Button, TextField, InputAdornment } from '@mui/material'; // Import the Grid, Button, and InputAdornment components
import Form from './Form';
import { Tooltip, Fab, Accordion, AccordionDetails, AccordionSummary, Checkbox, FormControlLabel, FormGroup, Input, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography } from "@mui/material";
import Box from '@mui/material/Box';
import Logo from "../assets/artifindlogo.png";
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';

const EditPage: React.FC = () => {
  const [forms, setForms] = useState([
    { id: 1, initialSearch: 'Initial value for Form 1', initialTime: 'Time 1' },
  ]);

  const [timeCycle, setTimeCycle] = useState('');

  const addForm = () => {
    const newFormId = forms.length + 1;
    const newForm = {
      id: newFormId,
      initialSearch: `Initial value for Form ${newFormId}`,
      initialTime: `Time ${newFormId}`,
    };
    setForms([...forms, newForm]);
  };

  const deleteForm = (id: number) => {
    setForms(forms.filter((form) => form.id !== id));
  };

  return (
    <div>
      <div className="Logo" style={{ display: 'flex', justifyContent: 'center', margin: '20px' }}>
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
      <h1>Edit Widgets</h1>
      <Grid container spacing={2}>
        {forms.map((form) => (
          <Grid item key={form.id} xs={12} md={6} lg={6}>
            <Form
              initialSearch={form.initialSearch}
              initialTime={form.initialTime}
              onDeleteForm={() => deleteForm(form.id)}
            />
          </Grid>
        ))}
      </Grid>

      {/* "Add Form" button */}
      <div style={{ position: 'fixed', bottom: '20px', left: '10px', display: 'flex', alignItems: 'center' }}>

        <Tooltip title="" arrow placement='top-start' sx={{ fontSize: "20px" }}>
          <Fab variant="extended" sx={{
            position: "fixed",
            bottom: "3%",
            right: "3%",
            backgroundColor: "#f15025",
            color: "white",
            '&:hover': {
              backgroundColor: "#191919",
            }
          }} onClick={addForm}>
            <AddCircleOutlineIcon sx={{ mr: 1 }} />
            Add form
          </Fab>
        </Tooltip>
      </div>
    </div>
  );
};

export default EditPage;