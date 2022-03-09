import React, { useState } from "react";

const Productos = () => {

    const initialState=[{
        id:1,
        name: "galleta",
        category:"abarrotes"
    },
    {
        id:2,
        name: "leche",
        category:"lacteos"
    },
    {
        id:3,
        name: "durazno",
        category:"abarrotes"
    }
]

const [product, setproduct]=useState(initialState);

return (
    <div>
        {product.map((producta)=>(
            <h2>{producta.name}</h2>
        ))}
    </div>
);
};

export default Productos;




