import React, {useState} from 'react';
import axios from 'axios';
import {  useNavigate } from 'react-router-dom';

const Register = () => 
{

    
    const [name,setName] = useState('')
    const [phone,setPhone] = useState('')
    const [email,setEmail] = useState('')
    const [dob,setDob] = useState('')

    const navigate = useNavigate()

    const handleSubmitForm = (e) => {
        e.preventDefault()
        const data={
            name:name,
            email:email,
            phone:phone,
            dob:dob
        }
        axios.post('http://54.87.235.156:8000/create-user/', data)

        .then(response=>{
         navigate('/home',  {state:{data:response.data.data}});
        })
        .catch((err)=>{
            if (err.response.data.msg === "Phone"){
                document.getElementById('phone').style.borderBlockColor="red";
            }
            else{
                console.log(err);
            }
        })
      }



    return (
        <div className='mainContainer'>
            
            <form className='Form-container' onSubmit={handleSubmitForm}>
                <input type='text' placeholder='Name' onChange={(e)=>{setName(e.target.value)}} value={name} required />
                <input type='email' placeholder='Email' onChange={(e)=>{setEmail(e.target.value)}} value={email} required />
                <input type="tel" placeholder='Phone number' id='phone' onChange={(e)=>{setPhone(e.target.value)}} value={phone} required />
                <input type='date' placeholder='D.O.B' onChange={(e)=>{setDob(e.target.value)}} value={dob} required />

                <div className="button">
                    <button type="submit"  className="btn btn-success">
                      Submit
                    </button>
                </div>
            </form>
        </div>
    );
}

export default Register;
