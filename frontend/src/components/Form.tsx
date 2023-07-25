import React, { useState } from 'react';
import './Form.css';
import { IconButton } from '@mui/material';
import { Delete as DeleteIcon } from '@mui/icons-material';

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

  const handleDeleteForm = () => {
    const confirmDelete = window.confirm('Are you sure you want to delete this form?');
    if (confirmDelete) {
      onDeleteForm();
    }
  };

  const iconButtonStyle: React.CSSProperties = {
    position: 'absolute',
    bottom: '10px',
    right: '10px',
    backgroundColor: 'red',
    color: '#fff',
    padding: '8px', // Adjust the padding to make the area smaller
    borderRadius: '50%', // Make the IconButton circular
  };

  return (
    <div className="form-box">
      <div className="form-content">
        <label>
          Search:
          <input
            type="text"
            value={search}
            onChange={handleSearchChange}
            onBlur={handleSubmit}
            className="form-input"
          />
        </label>
        <br />
        <label>
          Time:
          <input
            type="text"
            value={time}
            onChange={handleTimeChange}
            onBlur={handleSubmit}
            className="form-input"
          />
        </label>
      </div>

      {/* Replace the delete button with the delete icon */}
      <IconButton style={iconButtonStyle} onClick={handleDeleteForm}>
        <DeleteIcon />
      </IconButton>
    </div>
  );
};

export default Form;
