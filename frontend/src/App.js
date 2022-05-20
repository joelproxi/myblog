// import logo from './logo.svg';

import {
  BrowserRouter,
  Routes,
  Route,
 

} from "react-router-dom";


import './App.css';
import AddPostViews from "./views/AddPostViews";
import HomeViews from './views/HomeViews';
import PostdetailViews from "./views/PostdetailViews";





function App() {
  return (
    <BrowserRouter className='App'>
      <Routes>
        <Route  exact  path="/"   element={<HomeViews />} />
        <Route    path="post/:id"   element={<PostdetailViews />} />
        <Route    path="add"   element={ <AddPostViews /> } />
      </Routes> 
    </BrowserRouter>
    
  );
}

export default App;
