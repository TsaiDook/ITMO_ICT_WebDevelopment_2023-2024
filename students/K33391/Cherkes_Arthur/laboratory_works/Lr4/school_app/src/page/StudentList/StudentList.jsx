import React, { useCallback, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import useUser from "../../hooks/useUser";
import Student from "./Student";


function StudentList() {
  const navigate = useNavigate();
  const { token } = useUser();
  const [students, setStudents] = useState([]);

  const getStudents = useCallback(() => {
    fetch("http://localhost:8000/api/students/all/", {
      method: "GET",
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((result) => {
        setStudents(result);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, [token]);

  useEffect(() => getStudents(), [getStudents]);

  return (
    <div>
      {students ? (
        <>
          <Button
            onClick={() => navigate("/students/create")}
            variant="outline-primary"
          >
            Добавить ученика
          </Button>
          <div className="cell-group">
            {students.map((student, id) => (
              <Student student={student} getStudents={getStudents} key={id} />
            ))}
          </div>
        </>
      ) : (
        <></>
      )}
    </div>
  );
}

export default StudentList;