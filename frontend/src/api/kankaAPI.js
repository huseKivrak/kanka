import axiosInstance from "../auth/axiosInstance";

async function makeRequest(method, endpoint, data = null) {
  try {
    let response;

    if (method === "get" || method === "delete") {
      response = await axiosInstance[method](endpoint);
    } else {
      response = await axiosInstance[method](endpoint, data);
    }

    return response.data;
  } catch (error) {
    console.error(`Error in ${method} request to ${endpoint}:`, error);
    throw error;
  }
}

export const getLetters = () => makeRequest("get", "/api/letters/");

export const createLetter = (letterData) =>
  makeRequest("post", "/api/letters/", letterData);

export const getLetter = (id) => makeRequest("get", `/api/letters/${id}`);

export const updateLetter = (id, updates) =>
  makeRequest("put", `/api/letters/${id}`, updates);

export const deleteLetter = (id) => makeRequest("delete", `/api/letters/${id}`);

//get detail on delivered letter
export const readLetter = (id) =>
  makeRequest("get", `/api/letters/delivered/${id}/`);
