// Form.tsx (Updated)

import React, { useState } from 'react';
import './Form.css';

interface FormProps {
  initialSearch: string;
  initialTime: string;
}

const Form: React.FC<FormProps> = ({ initialSearch, initialTime }) => {
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
    position: 'absolute',
    top: '100px',
    right: '300px',
    backgroundColor: '#fff',
    border: '1px solid #ccc',
    padding: '10px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
  };

  return (

    
    <div className="form-box" style={{ width: '500px' }}> {/* Set the width of the form-box */}
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
    
  );
};

export default Form;
