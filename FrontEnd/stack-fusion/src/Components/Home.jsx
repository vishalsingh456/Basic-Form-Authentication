import React from 'react';
import { useLocation } from 'react-router-dom';

const Home = () => {

    const location = useLocation()

    return (
        
        <div className='details'>
            <h1>Your Details</h1>
            <h3>Name  : {location?.state?.data.name} </h3>
            <h3>Email : {location?.state?.data.email}</h3>
            <h3>Phone : {location?.state?.data.phone}</h3>
            <h3>DOB   : {location?.state?.data.dob}</h3>
            
        </div>
    );
}

export default Home;
