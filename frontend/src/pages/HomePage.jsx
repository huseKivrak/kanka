import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../context/AuthContext";
import { getLetters } from "../api/kankaAPI";

const HomePage = () => {
  let [letters, setLetters] = useState([]);

  useEffect(function getAndSetMailbox() {
    async function getLettersFromAPI() {
      let letters = await getLetters();
      console.log("letters: ", letters);
      setLetters(letters);
    }
    getLettersFromAPI();
  }, []);


  return (
    <div>
      <ul>
        {letters.map((letter) => (
          <a href={`/letters/${letter.id}`}><li key={letter.id}>{letter.title}</li></a>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
