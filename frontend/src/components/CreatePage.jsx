import React, { useState } from 'react';

const CreatePage = () => {
  const [itemName, setItemName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add your logic here to handle form submission (e.g., sending data to an API).
    console.log(`Item Name: ${itemName}`);
  };

  return (
    <div className="container mt-4">
      <h1>Create Item</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="itemName" className="form-label">Item Name</label>
          <input
            type="text"
            className="form-control"
            id="itemName"
            value={itemName}
            onChange={(e) => setItemName(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
};

export default CreatePage;





// import React from 'react';

// const CreatePage = () => {
//   return (
//     <h1>Hello</h1>
//   );
// };

// export default CreatePage;