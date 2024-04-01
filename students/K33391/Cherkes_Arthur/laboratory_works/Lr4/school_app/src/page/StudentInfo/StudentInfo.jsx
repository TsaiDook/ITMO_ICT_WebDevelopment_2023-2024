import React, { useCallback, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import useUser from "../../hooks/useUser";


function StudentInfo() {
    const [student, setStudent] = useState([]);
    const navigate = useNavigate();
    const { studentId } = useParams();
    const { token } = useUser();
    

    const getStudents = useCallback(() => {

    }, [studentId,token]);
    useEffect(() => {fetch(`http://127.0.0.1:8000/api/students/${studentId}`,{
        method: "GET",
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then(response => response.json())
        .then(data => {setStudent(data); console.log(data)})
        .catch(error => console.error('Ошибка:', error));}, [studentId, token, setStudent]);
  
    return (
      <div>
        <h3>{student.FIO}</h3>
        <p>Класс: {student.klass}</p>
        <h3>Оценки:</h3>
        <ul>
        {student.grades_set?.map(grade => (
          <li key={grade.id}>
            Оценка: {grade.grade}
          </li>
        ))}
      </ul>
        {/* <h2>Расписание:</h2>
        <ul>
          {student.schedules.map(schedule => (
            <li key={schedule}>Расписание {schedule}</li>
          ))}
        </ul>  */}
      </div>
    );
}

export default StudentInfo;