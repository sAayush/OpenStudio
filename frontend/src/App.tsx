import React from "react"
import { Route, BrowserRouter as Router, Routes } from "react-router-dom"

const App = () => {
  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/d" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App