import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter , Route, Routes} from 'react-router-dom';
import reportWebVitals from './reportWebVitals';

//Components:
import ProductList from './components/Productos/ProductList';

import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';


ReactDOM.render(
    <BrowserRouter>
    <div className='container my-4'>
        <Routes>
            <Route path='/' element={<ProductList />} /><Route/>
        </Routes>
    </div>
    </BrowserRouter>, 
document.getElementById('root'));

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
