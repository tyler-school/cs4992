// EditPage.tsx

import React, { useState } from 'react';
import Form from './Form';

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
      {forms.map((form) => (
        <div key={form.id} style={{ marginBottom: '20px' }}>
          <h2>Form {form.id}</h2>
          <Form
            initialSearch={form.initialSearch}
            initialTime={form.initialTime}
            onDeleteForm={() => deleteForm(form.id)}
          />
        </div>
      ))}
      <button onClick={addForm}>Add Another Form</button>
    </div>
  );
};

export default EditPage;
