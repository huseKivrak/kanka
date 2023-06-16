import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { readLetter } from "../api/kankaAPI";
import ErrorPage from "./ErrorPage";

const LetterDetail = () => {
  const { id } = useParams();
  const [letter, setLetter] = useState(null);

  useEffect(
    function getAndSetLetter() {
      async function getLetterFromAPI() {
        try {
          console.log("letterId:", id);
          let letter = await readLetter(id);
          setLetter(letter);
        } catch (error) {
          console.error(error);
          return <ErrorPage error={error} />;
        }
      }
      getLetterFromAPI();
    },
    [id]
  );

  return (
    <div>
      <h1>{letter?.title}</h1>
      <p>{letter?.date}</p>
      <p>{letter?.opener}</p>
      <p>{letter?.body}</p>
      <p>{letter?.closer}</p>
      <p>{letter?.signature}</p>
      <p>{letter?.postscript}</p>
    </div>
  );
};

export default LetterDetail;
