fetch("http://localhost:5001/events")
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
  });

document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.querySelector("#title").value;

  fetch("http://localhost:5001/events", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  })
  .then(response => response.json())
  .then(renderEvent)
  .catch(err => console.error("Fetch error:", err));
});

function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = event.title;
  document.querySelector("#event-list").appendChild(li);
}
