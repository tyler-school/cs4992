// Form.tsx (Updated)

import React, { useState } from 'react';
import './Form.css';

interface FormProps {
  initialSearch: string;
  initialTime: string;
  onDeleteForm: () => void;
}

const Form: React.FC<FormProps> = ({ initialSearch, initialTime, onDeleteForm }) => {
  const [search, setSearch] = useState(initialSearch);
  const [time, setTime] = useState(initialTime);
  const [submittedData, setSubmittedData] = useState<null | { search: string; time: string }>(
    null
  );

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearch(event.target.value);
  };

  const handleTimeChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setTime(event.target.value);
  };

  const handleSubmit = () => {
    const data = {
      search,
      time,
    };
    setSubmittedData(data);
  };

  const closePopup = () => {
    setSubmittedData(null);
  };

  //Change where the popup is here
  const popupStyle: React.CSSProperties = {
    position: 'fixed',
    top: '0',
    left: '50%',
    transform: 'translate(-50%)',
    backgroundColor: '#fff',
    border: '1px solid #ccc',
    padding: '10px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
  };

  const formStyle: React.CSSProperties = {
    position: 'relative',
    width: '500px',
  };

  const deleteButtonStyle: React.CSSProperties = {
    position: 'absolute',
    bottom: '10px',
    right: '10px',
    backgroundColor: 'red',
    color: '#fff',
    padding: '8px 12px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  };

  const handleDeleteForm = () => {
    const confirmDelete = window.confirm('Are you sure you want to delete this form?');
    if (confirmDelete) {
      onDeleteForm();
    }
  };

  return (
    <div style={formStyle}>
      <div className="form-box">
        <label>
          Search:
          <input type="text" value={search} onChange={handleSearchChange} />
        </label>
        <br />
        <label>
          Time:
          <input type="text" value={time} onChange={handleTimeChange} />
        </label>

        <br />
        <button onClick={handleSubmit}>Submit</button>

        {/* Display pop-up with submitted data */}
        {submittedData && (
          <div style={popupStyle}>
            <h2>Submitted Data</h2>
            <p>Search: {submittedData.search}</p>
            <p>Time: {submittedData.time}</p>
            <button onClick={closePopup}>Close</button>
          </div>
        )}
      </div>

      <button style={deleteButtonStyle} onClick={handleDeleteForm}>
        Delete Form
      </button>
    </div>
  );
};

export default Form;
