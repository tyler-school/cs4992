// EditPage.tsx (Updated)

import React, { useState } from 'react';
import { Grid, Button } from '@mui/material'; // Import the Grid and Button components
import Form from './Form';
import { IconButton } from '@mui/material';
import AddCircleIcon from '@mui/icons-material/AddCircle';
const EditPage: React.FC = () => {
  const [forms, setForms] = useState([
    { id: 1, initialSearch: 'Initial value for Form 1', initialTime: 'Time 1' },
  ]);

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
      <div style ={{ position: 'fixed', bottom: '20px', left: '20px'}}>
        <IconButton style={{ fontSize: '50', color: 'green'}} onClick={addForm}>
          <AddCircleIcon />
        </IconButton>
      </div>
      

      {/* Home button */}
      <div style={{ position: 'fixed', bottom: '20px', right: '20px' }}>
        <Button variant="contained" color="primary" component="a" href="/">
          Home
        </Button>
      </div>
    </div>
  );
};

export default EditPage;

//FAB import that make sure 
//Import icons too
