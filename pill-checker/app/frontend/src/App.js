import React, { useEffect, useState } from "react"
import { AllPills } from './components/allPills'
import { PillUpload } from "./components/uploadPill";
import {Link, Routes, Route, useNavigate} from 'react-router-dom';

const App = () => {

  return (
    <div className="App">
    <AllPills></AllPills>
    <PillUpload></PillUpload>
    </div>
  );
}

export default App;