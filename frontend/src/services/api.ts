import axios from "axios"

const API_URL = "http://localhost:8000/api/accounts/"

export interface RegisterData {
  username: string
  email: string
  first_name?: string
  last_name?: string
  password: string
}

export interface LoginData {
  email: string
  password: string
}

export const registerUser = (userData: RegisterData) => axios.post(`${API_URL}register/`, userData)
export const loginUser = (credentials: LoginData) => axios.post(`${API_URL}token/`, credentials)
