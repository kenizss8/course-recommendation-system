import axios from 'axios'

const API_BASE_URL = 'http://127.0.0.1:8000'

export const getCourses = async () => {
  const response = await axios.get(`${API_BASE_URL}/courses`)
  return response.data
}

export const getRecommendations = async (payload) => {
  const response = await axios.post(`${API_BASE_URL}/recommend`, payload)
  return response.data
}
