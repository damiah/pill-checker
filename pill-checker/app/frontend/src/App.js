import React, { useEffect, useState } from "react"
import { AllPills } from './components/allPills'
import { Form } from "./components/uploadPillForm";
// import {Link, Routes, Route, useNavigate} from 'react-router-dom';

const App = () => {

  return (
    <div className="App">
    <AllPills></AllPills>
    <Form></Form>
    </div>
  );
}

export default App;