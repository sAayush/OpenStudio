import React from "react"
import { Route, BrowserRouter as Router, Routes } from "react-router-dom"
import Home from "./pages/Home"
import Profile from "./pages/Profile"

const App = () => {
  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/d" element={<Profile />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
