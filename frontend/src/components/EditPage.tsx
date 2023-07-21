// Form.tsx (Same component as defined before)

// App.tsx (Parent component)
import React from 'react';
import Form from './Form';

const EditPage: React.FC = () => {
  return (
    <div>
      <h1>Multiple Forms Example</h1>
      <div style={{ marginBottom: '20px' }}>
        <h2>Form 1</h2>
        <Form initialSearch="Initial value for Form 1" initialTime="Time 1" />
      </div>
      <div>
        <h2>Form 2</h2>
        <Form initialSearch="Initial value for Form 2" initialTime="Time 2" />
      </div>
    </div>
  );
};

export default EditPage;
