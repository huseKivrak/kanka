import { useState } from "react";
import { createLetter } from "../api/kankaAPI";
import { Navigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";
const LetterForm = () => {
  const [letter, setLetter] = useState({
    title: "",
    body: "",
    date: "",
    opener: "",
    closer: "",
    signature: "",
    postscript: "",
  });

  const { user } = useContext(AuthContext);

  const handleChange = (event) => {
    setLetter({
      ...letter,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    letter.status = "DRAFT";
    letter.author = user.username;
    console.log("letter:", letter);
    const newLetter = await createLetter(letter);
    console.log("newLetter:", newLetter);
    if (newLetter.id) {
      return <Navigate to={`/letters/${newLetter.id}`} replace />;
    }
  };

  return (
    <div>
      <h1>Letter Form</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="title">Title</label>
        <input
          id="title"
          name="title"
          type="text"
          value={letter.title}
          onChange={handleChange}
        />
        <label htmlFor="body">Body</label>
        <textarea
          id="body"
          name="body"
          type="text"
          value={letter.body}
          onChange={handleChange}
        />
        <label htmlFor="date">Date</label>
        <input
          id="date"
          name="date"
          type="text"
          value={letter.date}
          onChange={handleChange}
        />
        <label htmlFor="opener">Opener</label>
        <input
          id="opener"
          name="opener"
          type="text"
          value={letter.opener}
          onChange={handleChange}
        />
        <label htmlFor="closer">Closer</label>
        <input
          id="closer"
          name="closer"
          type="text"
          value={letter.closer}
          onChange={handleChange}
        />
        <label htmlFor="signature">Signature</label>
        <input
          id="signature"
          name="signature"
          type="text"
          value={letter.signature}
          onChange={handleChange}
        />
        <label htmlFor="postscript">Postscript</label>
        <input
          id="postscript"
          name="postscript"
          type="text"
          value={letter.postscript}
          onChange={handleChange}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default LetterForm;
