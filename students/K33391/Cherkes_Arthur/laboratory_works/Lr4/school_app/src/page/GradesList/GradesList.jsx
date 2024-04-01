import React, { useCallback, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import useUser from "../../hooks/useUser";
import Grades from "./Grades";


function GradesList() {
  const navigate = useNavigate();
  const { token } = useUser();
  const [grades, setGrades] = useState([]);

  const getGrades = useCallback(() => {
    fetch("http://localhost:8000/api/grades/all/", {
      method: "GET",
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((result) => {
        setGrades(result);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, [token]);

  useEffect(() => getGrades(), [getGrades]);

  return (
    <div>
      {grades ? (
        <>
          <Button
            onClick={() => navigate("/grades/create")}
            variant="outline-primary"
          >
            Добавить оценку
          </Button>
          <div className="cell-group">
            {grades.map((grade, id) => (
              <Grades grade={grade} getGrades={getGrades} key={id} />
            ))}
          </div>
        </>
      ) : (
        <></>
      )}
    </div>
  );
}

export default GradesList;