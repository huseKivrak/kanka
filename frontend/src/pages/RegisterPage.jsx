import { useState } from "react";

const RegisterPage = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    passwordConfirm: "",
  });

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("formData:", formData);

    if (formData.password !== formData.passwordConfirm) {
      alert("Passwords do not match. Please try again.");
      return;
    }
  };

  return (
    <div>
      <h1>Register</h1>

      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username</label>
        <input
          id="username"
          value={formData.username}
          name="username"
          type="text"
          onChange={handleChange}
        />
        <label htmlFor="password">Password</label>
        <input
          id="password"
          value={formData.password}
          name="password"
          type="password"
          onChange={handleChange}
        />
        <label htmlFor="passwordConfirm">Confirm Password</label>
        <input
          id="passwordConfirm"
          value={formData.passwordConfirm}
          name="passwordConfirm"
          type="password"
          onChange={handleChange}
        />
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default RegisterPage;
