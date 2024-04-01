import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import useUser from "../../hooks/useUser";
import Header from "../../components/Header";
import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";
import StudentList from "../StudentList";
import GradesList from "../GradesList/GradesList";



function Main() {
  const navigate = useNavigate();
  const [user, setUser] = useState([]);
  const [data, setData] = useState([]);
  const { token } = useUser();

  useEffect(() => {
    fetch("http://localhost:8000/api/auth/users/me", {
      method: "GET",
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((result) => {
        setUser(result);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, [token]);

  return (
    <>
      <Header username={user.username} />
      <div className="main-container container">
        <Tabs
          defaultActiveKey="Students"
          id="uncontrolled-tab-example"
          className="mb-3"
        >
          <Tab eventKey="Students" title="Ученики">
            <StudentList />
          </Tab>
          <Tab eventKey="Grades" title="Оценки">
            <GradesList />
          </Tab>
        </Tabs>
      </div>
    </>
  );
}

export default Main;