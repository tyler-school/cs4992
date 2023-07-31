import React, { useState } from 'react';
import { Grid, Button, TextField, InputAdornment } from '@mui/material'; // Import the Grid, Button, and InputAdornment components
import Form from './Form';
import { IconButton } from '@mui/material';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import Box from '@mui/material/Box';
import Logo from "../assets/artifindlogo.png";

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
      <h1>Multiple Forms Example</h1>
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
      <div style={{ position: 'fixed', bottom: '20px', left: '20px', display: 'flex', alignItems: 'center' }}>

        <IconButton style={{ fontSize: '50', color: 'green' }} onClick={addForm}>
          <AddCircleIcon />
        </IconButton>
      </div>
    </div>
  );
};

export default EditPage;
