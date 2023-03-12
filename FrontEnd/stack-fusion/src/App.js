import './App.css';
import Register from './Components/Register';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import Home from './Components/Home';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Register/>} />
          <Route path='/home' element={<Home />} />
        </Routes>
        
      </BrowserRouter>
    </div>
  );
}

export default App;
