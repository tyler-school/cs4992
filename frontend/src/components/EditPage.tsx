import React, { useState } from 'react';
import { Grid, Button, TextField, InputAdornment } from '@mui/material'; // Import the Grid, Button, and InputAdornment components
import Form from './Form';
import { IconButton } from '@mui/material';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import HomeIcon from '@mui/icons-material/Home'; // Import the HomeIcon

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

      {/* Time Cycle input and "Add Form" button */}
      <div style={{ position: 'fixed', bottom: '20px', left: '20px', display: 'flex', alignItems: 'center' }}>
        <TextField
          label="Time"
          value={timeCycle}
          onChange={(e) => setTimeCycle(e.target.value)}
          variant="outlined"
          style={{ width: '150px', marginRight: '10px', backgroundColor: '#fff' }}
          InputProps={{
            endAdornment: <InputAdornment position="end">seconds</InputAdornment>,
          }}
        />

        <IconButton style={{ fontSize: '50', color: 'green' }} onClick={addForm}>
          <AddCircleIcon />
        </IconButton>
      </div>

      {/* Home button */}
      <div style={{ position: 'fixed', bottom: '20px', right: '20px' }}>
        <Button variant="contained" color="primary" component="a" href="/">
          <HomeIcon /> Home
        </Button>
      </div>
    </div>
  );
};

export default EditPage;
