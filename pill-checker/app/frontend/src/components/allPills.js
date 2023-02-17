import React, { useEffect, useState } from "react"

export const AllPills = () => {
  const [pills, setPills] = useState([])
  
  const fetchPillData = () => {
    fetch("/pills")
      .then(response => response.json())
      .then(response => JSON.parse(response))
      .then(data => {
        setPills(data)
      })
  }

  useEffect(() => {
    fetchPillData()
  }, [])

  return (
    <div>
      {pills.length > 0 && (
        <ul>
          {pills.map(pill => (
            <li key={pill.Name}><h1><b>{pill.Name}</b></h1>
            <li key={pill.Name}>{pill.Description}</li>
            </li>
          ))}
      </ul>
      )}
    </div>
  );
}
