import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const submitLoanApplication = async (applicationData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/submit-application`, applicationData);
    return response.data;
  } catch (error) {
    console.error('Error in API service:', error);
    throw error;
  }
};
