import React, { useCallback, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import useUser from "../../hooks/useUser";


function Grades({ grade, getGrades }) {
  const navigate = useNavigate();
  const { token } = useUser();
  const [routeData, setRouteData] = useState("");

  const onDelete = (grade) => {
    fetch(`http://127.0.0.1:8000/api/grades/delete/${grade.id}/`, {
      method: "DELETE",
      headers: {
        Authorization: `Token ${token}`,
      },
    }).then(() => getGrades());
  };

  return (
    <div className="cell-container">
      <div>
        <div>
           <div>
              Оценка: {grade.grade}
            </div>
            <div>
              ID ученика: {grade.student}
            </div>
            <div>
              ID расписания: {grade.schedule}
            </div>
        </div> 
      </div>
      <div className="cell-route">
        
        <div>{routeData.destination_point}</div>
      </div>
      <div className="cell-button-group">
        {/* <btn
          className="cell-button"
          onClick={() => navigate(`student/edit/${student.id}`)}
        /> */}

        <Button
            onClick={() => navigate(`grade/update/${grade.id}`)}
            variant="outline-primary"
          >
            Редактировать
          </Button>

        <Button
            onClick={() => onDelete(grade)}
            variant="outline-primary"
          >
            Удалить
          </Button>
      </div>
    </div>
  );
}

export default Grades;