import React, {useState} from 'react';
import {Link, Routes, Route, Redirect} from 'react-router-dom';

export const PillUpload = () => {
    // const navigate = useNavigate();

    const handleSubmit = event => {
      event.preventDefault();
  
      // 👇️ redirect to /contacts
      navigate('/contacts');
    };
    
	return(
   <div>
    
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="file" type="file" multiple></input>
    <input type="submit"></input>
    </form>
    
	</div>
	)
}