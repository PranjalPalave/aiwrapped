const sendButton = document.getElementById("sendButton");
const solution = document.getElementById("solution");
const questionInputElement = document.getElementById("questionInput");

async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return response.json();
}

sendButton.addEventListener("click", async () => {
  const questionInput = questionInputElement.value.trim();
  if (!questionInput) return;

  // Clear textarea and show loading
  questionInputElement.value = "";
  solution.innerHTML = "Analyzing your essay...";
  document.querySelector(".right2").style.display = "block";
  document.querySelector(".right1").style.display = "none";

  try {
    let result = await postData("/api", { question: questionInput });
    solution.innerHTML = result.answer ?? "No answer received.";
  } catch (error) {
    solution.innerHTML = "Error occurred. Please try again.";
    console.error(error);
  }
});
