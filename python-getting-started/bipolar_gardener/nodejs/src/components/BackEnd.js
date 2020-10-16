import React, { useEffect } from "react";
import axios from "axios";

const url = "http://127.0.0.1:8000/";
const BackEnd = (data) => {
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(url);
      const data = await response.json();
      return data
      // END fetchData
    };
    const sendUserData = async () => {
      const userData = data.props;
      const sendIt = await axios.post(url, { data: userData });
     console.log(sendIt)
      //END sendUserData
    };
    sendUserData();
    fetchData();

    //END useEffect
  }, [data]);

  return <h1> Im the backend </h1>;
};

export default BackEnd;
