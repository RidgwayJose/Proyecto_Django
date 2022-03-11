import React, { useEffect, useState } from 'react';


//Components

import * as ProductServer from './ProductServer';

const trStyle = {
    textAlign: 'center',
  }

const ProductList = () => {
    const [products, setProducts] = useState([]);

    const listProducts= async ()=>{
        try {
            const res = await ProductServer.listProducts();
            console.log(res);
            const data = await res.json();
            setProducts(data);
            console.log(data);
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(()=>{
    listProducts();
    },[]);
    

    
    return (
        <div>
            <div className="card-body d-flex">
            <h2>LISTA DE PRODUCTOS</h2>  
            <a className="btn btn-primary ml-auto" role="button" type ="submit" href="crear">Agregar</a>
            </div>
            <div>
            <table className="table table-striped" style={trStyle}>
                <thead>
                    <tr>
                        <th>Codigo</th>
                        <th>Producto</th>
                        <th>Marca</th>
                        <th>Categoria</th>
                        <th>Precio</th>
                        <th>Stock</th>
                        <th>Imagen</th>
                        <th>Opciones</th>
                    </tr>
                </thead>
                <tbody>
                {products.map((producto) => (
                    <tr > 
                        <td>{producto.name}</td>
                        <td>{producto.name}</td>
                        <td>{producto.category}</td>
                        <td>{producto.brand}</td>
                        <td>{producto.price}</td>
                        <td>{producto.stock}</td>
                        <td><img src="" alt=""></img></td>
                        <td>
                            <a className="btn btn-primary" href="https://www.digitalocean.com/community/tutorials/how-to-create-react-elements-with-jsx-es" role="button"><img src="https://cdn-icons-png.flaticon.com/512/45/45406.png" alt = "description" width="30px"></img></a>
                            <a className="btn btn-danger" role="button" href="https://www.digitalocean.com/community/tutorials/how-to-create-react-elements-with-jsx-es"><img src="https://cdn-icons-png.flaticon.com/512/88/88666.png" alt = "description 2" width="30px"></img></a>
                        </td>
                    </tr> ))}
                </tbody>
            </table>
            </div>
        </div>    
    )
};

export default ProductList;