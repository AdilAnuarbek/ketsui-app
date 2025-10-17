import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [tasks, setTasks] = useState([]);
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/tasks')
        .then(res => {
            setTasks(res.data);
        })
        .catch(err => {
            console.error("There was an error fetching tasks", err);
        });
    }, []);
    return (
        <div className="App">
            <h1>Task List</h1>
            <ul>
                {tasks.map((task) => (
                    <li key={task.id}>
                        <h3>{task.title}</h3>
                        <p>{task.description}</p>
                        <p>Status: {task.completed ? 'Completed' : 'Pending'}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}
export default App;