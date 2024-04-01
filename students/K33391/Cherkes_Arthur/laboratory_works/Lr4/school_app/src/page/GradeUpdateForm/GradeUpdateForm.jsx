import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import useUser from "../../hooks/useUser";
import { Form, Button, Row, Col } from "react-bootstrap";

const GradeUpdateForm = () => {
  const { gradeId } = useParams();
  const { setToken, token } = useUser();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    schedule: null,
    student: null,
    grade: null,
    attendanse: true,

  });

  const [availableSchedules, setAvailableSchedules] = useState([]);
  const [availableStudents, setAvailableStudents] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/grades/${gradeId}`)
      .then((response) => response.json())
      .then((gradeData) => {
        setFormData(gradeData);
      })
      .catch((error) => console.error("Error fetching grade data:", error));

      fetch("http://127.0.0.1:8000/api/schedules/all", {
        method: "GET",
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => response.json())
        .then((result) => {
          setAvailableSchedules(result);
        })
        .catch((error) => console.error("Error fetching data:", error));
  
      fetch("http://127.0.0.1:8000/api/students/all", {
          method: "GET",
          headers: {
            Authorization: `Token ${token}`,
          },
        })
          .then((response) => response.json())
          .then((result) => {
            setAvailableStudents(result);
          })
          .catch((error) => console.error("Error fetching data:", error));
  }, [gradeId, token]);

  const handleChange = (event) => {
    const { name, value } = event.target;
      setFormData({
        ...formData,
        [name]: value,
      });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    fetch(`http://127.0.0.1:8000/api/grades/update/${gradeId}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((updatedFlight) => {
        console.log("Grade updated successfully:", updatedFlight);
        navigate("/");
      })
      .catch((error) => console.error("Error updating grade:", error));
  };

  return (
    <div className="container mt-4">
      <h2>Оценка</h2>
      <Form onSubmit={handleSubmit}>
        <Row className="mb-3">
            <Form.Group controlId="student">
                <Form.Label>Оценка:</Form.Label>
                        <Form.Control
                    type="text"
                    name="grade"
                    value={formData.grade}
                    onChange={handleChange}
                />
            </Form.Group>
        </Row>

        <Form.Group controlId="student">
          <Form.Label>Ученик:</Form.Label>
          <Form.Select
            name="student"
            value={formData.student}
            onChange={handleChange}
          >
            <option value="">Выбор ученика</option>
            {availableStudents.map((student) => (
              <option key={student.id} value={student.id}>
                {student.FIO} 
              </option>
            ))}
          </Form.Select>
        </Form.Group>

        <Form.Group controlId="schedule">
          <Form.Label>Расписание:</Form.Label>
          <Form.Select
            name="schedule"
            value={formData.schedule}
            onChange={handleChange}
          >
            <option value="">Выбор расписания</option>
            {availableStudents.map((schedule) => (
              <option key={schedule.id} value={schedule.id}>
                {schedule.id} {schedule.date} 
              </option>
            ))}
          </Form.Select>
        </Form.Group>

        <Button variant="primary" type="submit">
          Обновить
        </Button>
        <Button
          variant="primary"
          onClick={() => {
            navigate("/");
          }}
          className="m-3"
        >
          На главную
        </Button>
      </Form>
    </div>
  );
};

export default GradeUpdateForm;