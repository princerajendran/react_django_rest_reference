// import React from 'react';


// const ListPage = () => {
//     return (
//         <h1>Item List</h1>
//     );
// };

// export default ListPage;


import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ListPage = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from your API endpoint using Axios
    axios.get('http://127.0.0.1:8000/todo/todos/') // Replace with your API URL
      .then((response) => {
        setData(response.data);
        setLoading(false);
        console.log(data);
      })
      .catch((error) => {
        console.error(error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="container mt-4">
      <h1>Item List</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul className="list-group">
          {data.map((item) => (
            <li className="list-group-item" key={item.id}>
               {item.todo_name + ' - ' + item.todo_name + ' - ' + item.status}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ListPage;

