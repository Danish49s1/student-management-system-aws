const API_URL = "https://h8xptw0wxf.execute-api.us-east-1.amazonaws.com/prod/students";

// Add Student
function addStudent() {
  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: document.getElementById("name").value,
      age: document.getElementById("age").value,
      course: document.getElementById("course").value
    })
  })
    .then(res => res.json())
    .then(data => {
      console.log("Add response:", data);
      // Some Lambda responses wrap data inside 'body'
      if (data.body) {
        data = JSON.parse(data.body);
      }
      alert("Student Added: " + data.studentId);
    });
}

function getStudents() {
  fetch(API_URL, { method: "GET" })
    .then(res => res.json())
    .then(data => {
      console.log("Raw response:", data);
      // If API Gateway wraps response inside "body", parse it
      if (data.body) {
        data = JSON.parse(data.body);
      }
      document.getElementById("output").innerText = JSON.stringify(data, null, 2);
    })
    .catch(err => {
      console.error("Error fetching students:", err);
      document.getElementById("output").innerText = "Error fetching students.";
    });
}
// Update Student
function updateStudent() {
  fetch(API_URL, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      studentId: document.getElementById("updateId").value,
      name: document.getElementById("updateName").value,
      age: document.getElementById("updateAge").value,
      course: document.getElementById("updateCourse").value
    })
  })
    .then(res => res.json())
    .then(data => {
      console.log("Update response:", data);
      if (data.body) {
        data = JSON.parse(data.body);
      }
      alert("Student Updated: " + JSON.stringify(data));
    });
}

// Delete Student
function deleteStudent() {
  fetch(API_URL, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      studentId: document.getElementById("deleteId").value
    })
  })
    .then(res => res.json())
    .then(data => {
      console.log("Delete response:", data);
      if (data.body) {
        data = JSON.parse(data.body);
      }
      alert(data.message);
    });
}