import axiosInstance from "./axiosInstance";

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

export const getLetters = () => makeRequest("get", "/letters/");

export const createLetter = (letter) =>
  makeRequest("post", "/letters/", letter);

export const getLetter = (id) => makeRequest("get", `/letters/${id}`);

export const updateLetter = (id, updates) =>
  makeRequest("put", `/letters/${id}`, updates);

export const deleteLetter = (id) => makeRequest("delete", `/letters/${id}`);
