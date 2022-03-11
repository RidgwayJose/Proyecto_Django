const API_URL = "http://127.0.0.1:8000/productos/prod/"

export const listProducts = async () => {
    return await fetch(API_URL)
}